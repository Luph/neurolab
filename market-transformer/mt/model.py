"""Cross-asset transformer.

Every asset is a token.  A token is built from that asset's recent vol-normalised history
(a 20-day patch plus slower summaries), a learned asset embedding and an asset-class embedding.
Self-attention across the ~370 tokens lets any asset's representation depend non-linearly on the
state of every other asset.

Two heads are trained as separate models:
  * "predict": forecasts forward returns (t+1, t+2, t+2..t+6) from information at the close of t.
  * "fair"   : masked-asset model. Same-day moves of a random 1/8 of assets are hidden; the model
               reconstructs them from everyone else's same-day moves + history.  At inference each
               asset is hidden once, giving a non-linear, cross-asset "fair" move; actual - fair is
               the residual used for mispricing detection.
"""
import torch
import torch.nn as nn


class CrossAssetTransformer(nn.Module):
    def __init__(self, n_assets, n_classes, n_feat, n_out, d=48, heads=4, layers=2, ff=96, dropout=0.1):
        super().__init__()
        self.inp = nn.Sequential(nn.Linear(n_feat, d), nn.GELU(), nn.Linear(d, d))
        self.asset_emb = nn.Embedding(n_assets, d)
        self.class_emb = nn.Embedding(n_classes, d)
        self.market_tok = nn.Parameter(torch.zeros(1, 1, d))
        layer = nn.TransformerEncoderLayer(d, heads, ff, dropout, batch_first=True, norm_first=True,
                                           activation="gelu")
        self.enc = nn.TransformerEncoder(layer, layers, enable_nested_tensor=False)
        self.norm = nn.LayerNorm(d)
        self.head = nn.Linear(d, n_out)
        nn.init.normal_(self.asset_emb.weight, std=0.02)
        nn.init.normal_(self.class_emb.weight, std=0.02)

    def forward(self, x, asset_ids, class_ids, pad_mask):
        # x: (B, N, F); pad_mask: (B, N) True where the asset does not exist yet
        h = self.inp(x) + self.asset_emb(asset_ids)[None] + self.class_emb(class_ids)[None]
        B = h.shape[0]
        h = torch.cat([self.market_tok.expand(B, -1, -1), h], 1)
        pm = torch.cat([torch.zeros(B, 1, dtype=torch.bool, device=x.device), pad_mask], 1)
        h = self.enc(h, src_key_padding_mask=pm)
        return self.head(self.norm(h[:, 1:]))
