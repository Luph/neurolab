#!/usr/bin/env python3
"""Scan a chapter .tex file for banned patterns from standards.md Section 8.

Usage: python3 scripts/scan_prose.py chapters/NN-slug.tex [--all]
Reports each hit with line number. Clause environments, excel blocks, equations and
quoted [BAD] examples are skipped. Technical senses (leverage = debt, critical path, fuel
as gas, key performance indicators, comprehensive cover, stakeholder engagement) are
whitelisted by context patterns. Exit code 1 if hits found.
"""
import re, sys

WORDS = r"""delve|dive into|unpack|embark|unlock|unleash|harness|empower|elevate|streamline|supercharge|foster|bolster|underscore|underscores|showcase|spotlight|resonate|boasts?|utilize|utilise|utilization|facilitate|revolutionize|reimagine|redefine|lean into|grapple with|wrestle with|weave|curate|spearhead|embrace|encompass|elucidate|illuminate|commence|endeavor|ignite|propel|skyrocket|soar|thrive|flourish|double down|landscape|realm|sphere|ecosystem|tapestry|journey|testament|beacon|cornerstone|bedrock|linchpin|hallmark|catalyst|crucible|nexus|interplay|intricacies|synergy|paradigm|game-changer|plethora|myriad|learnings|deep dive|bandwidth|crucial|pivotal|vital|paramount|imperative|indispensable|robust|seamless|seamlessly|holistic|multifaceted|intricate|granular|vibrant|bustling|nestled|meticulous|meticulously|commendable|noteworthy|invaluable|impactful|insightful|actionable|transformative|revolutionary|groundbreaking|cutting-edge|state-of-the-art|next-generation|innovative|unparalleled|world-class|best-in-class|ever-evolving|ever-changing|fast-paced|burgeoning|daunting|seasoned|savvy|quintessential|unwavering|steadfast|fascinating|compelling|exciting|aforementioned|truly|genuinely|incredibly|deeply|profoundly|remarkably|undeniably|absolutely|arguably|indeed|inherently|intrinsically|fundamentally|essentially|ultimately|notably|importantly|crucially|interestingly|various|numerous|a wide array of|a diverse range of|a plethora of|a myriad of|a number of|very|extremely|highly|particularly|really|in order to|due to the fact that|the fact that|at this point in time|each and every|with regard to|in terms of|basically|in a nutshell|in essence|simply put|put simply|navigate|navigating|tailored"""
PHRASES = [
 "in today's", "ever-evolving landscape", "in an era of", "now more than ever", "gone are the days", "it's no secret",
 "imagine a world", "picture this", "have you ever wondered", "at first glance", "when it comes to", "in the world of",
 "at its core", "at the heart of", "let's dive", "let's break", "let's unpack", "let's take a closer look", "here's the thing",
 "here's where it gets", "here's the kicker", "here's the catch", "here's how it works", "here's why", "this is where",
 "with that in mind", "that said", "that being said", "having said that", "against this backdrop", "in light of this",
 "moving forward", "going forward", "first and foremost", "last but not least", "needless to say", "it goes without saying",
 "not to mention", "it's worth noting", "it is worth noting", "it's important to note", "it is important to note", "it bears mentioning",
 "as we've seen", "as mentioned earlier", "as discussed earlier", "in this section, we", "in this chapter, we", "in this chapter we", "in the next chapter",
 "now let's turn", "so, what does this mean", "why does this matter", "the truth is", "the reality is", "the fact of the matter",
 "make no mistake", "let's face it", "let's be honest", "to be clear", "in other words", "the key is", "what sets",
 "there's a reason", "it's no wonder", "begs the question", "raises important questions", "the bottom line is", "the short answer",
 "the answer?", "the result?", "the catch?", "the best part?", "spoiler:", "let that sink in", "read that again", "full stop",
 "this changes everything", "and that's the point", "and that's okay", "this is huge", "in conclusion", "in summary", "to sum up",
 "all in all", "overall,", "at the end of the day", "when all is said and done", "one thing is certain", "it remains to be seen",
 "only time will tell", "the possibilities are endless", "the lesson is clear", "this serves as a reminder", "cautionary tale",
 "food for thought", "only the beginning", "little did", "would change everything", "not only", "plays a crucial role",
 "plays a key role", "plays a vital role", "is a key component", "is a critical factor", "serves as", "stands as", "functions as",
 "may potentially", "could possibly", "can often", "generally speaking", "it is generally considered", "to some extent", "in a sense",
 "in many ways", "it's fair to say", "it's safe to say", "double-edged sword", "perfect storm", "tip of the iceberg", "elephant in the room",
 "delicate balance", "balancing act", "walking a tightrope", "striking a balance", "uncharted waters", "high-stakes", "game of chess",
 "david and goliath", "house of cards", "ticking time bomb", "canary in the coal mine", "wake-up call", "sent shockwaves", "writing was on the wall",
 "hindsight is", "the rest is history", "a far cry from", "par for the course", "the name of the game", "lion's share", "moving target",
 "easier said than done", "grand scheme", "move the needle", "low-hanging fruit", "hit the ground running", "next level", "raise the bar",
 "set the stage", "pave the way", "paving the way", "stand the test of time", "shed light", "jury is still out", "keeps them up at night",
 "stakes have never been higher", "seismic shift", "treasure trove", "hidden gem", "touch base", "circle back", "devil is in the details",
 "cash is king", "follow the money", "no free lunch", "go hand in hand", "more art than science", "an art and a science", "lifeblood",
 "a textbook example", "masterclass", "holy grail", "secret sauce", "unsung hero", "silent killer", "murphy's law", "north star",
 "roadmap", "well-oiled machine", "building blocks", "the fabric of", "think of it as", "think of x as", "it was then that", "in that moment",
 "something shifted", "suddenly, it all", "everything was on the line", "it all came down to", "against all odds", "a breath she didn't know",
 "raised an eyebrow", "raised eyebrow", "wry smile", "leaned back in", "exchanged glances", "ran a hand through", "steepled", "heavy silence",
 "fell silent", "hung in the air", "great question", "you're probably wondering", "you might be thinking", "don't worry", "fear not",
 "rest assured", "you've got this", "may sound intimidating", "easier than it sounds", "to be frank", "candidly", "i'll be honest",
 "pay close attention", "in layman's terms", "in plain english", "studies show", "research suggests", "experts agree", "many believe",
 "it is widely recognized", "industry insiders", "a staggering", "a whopping", "eye-watering", "a mere", "no one-size-fits-all",
 "every deal is different", "consult a qualified", "this is not legal advice", "as of my last", "i hope this helps", "let me know",
 "sarah chen", "elena vasquez", "marcus thorne", "aris thorne", "elara vance", "veridia", "eldoria", "solara",
 "highlighting the importance", "underscoring the", "reflecting a broader", "making it a cornerstone", "it's not just", "isn't just", "more than just",
 "furthermore", "moreover", "additionally",
]
HEADING_BAD = re.compile(r"\\(?:chapter|section|subsection|subsubsection)\*?\{(?:Understanding|Exploring|A Closer Look|Demystifying|Unlocking|Mastering|Navigating|Beyond|The Art of|The Power of|The Anatomy of|The Role of|The Importance of|Why .* Matters|The Secret|Key Takeaways|Final Thoughts|Wrapping Up|Looking Ahead|The Road Ahead|The Bottom Line|Putting It All Together|Everything You Need)", re.I)
WHITELIST = re.compile(r"critical path|key performance indicator|comprehensive cover|stakeholder engagement|fuel supply|fuel cost|fuel price|fuel charge|fuel pass|fuel oil|leverage ratio|leverage effect|operating leverage|financial leverage|highly rated|indeed[^a-z]*\\\\cite", re.I)

SKIP_ENV = re.compile(r"\\begin\{(clause|clausevariant|pfclausebox|excel|lstlisting|equation\*?|align\*?|tikzpicture|sources)\}")
END_ENV = re.compile(r"\\end\{(clause|clausevariant|pfclausebox|excel|lstlisting|equation\*?|align\*?|tikzpicture|sources)\}")

def main(path):
    txt = open(path, encoding="utf-8").read().splitlines()
    hits = []
    depth = 0
    word_re = re.compile(r"\b(" + WORDS + r")\b", re.I)
    para_dashes = 0; para_start = 1
    for i, line in enumerate(txt, 1):
        if SKIP_ENV.search(line): depth += 1
        if depth == 0 and not line.lstrip().startswith("%"):
            low = line.lower()
            if "[bad]" in low: continue
            scrub = WHITELIST.sub("", line)
            for m in word_re.finditer(scrub):
                hits.append((i, "word", m.group(0)))
            for p in PHRASES:
                if p in scrub.lower():
                    hits.append((i, "phrase", p))
            if HEADING_BAD.search(line): hits.append((i, "heading", line.strip()[:80]))
            if "!" in re.sub(r"\\[a-zA-Z]+|!\s*$", "", line) and not line.strip().startswith("\\"):
                if re.search(r"[A-Za-z]!", line): hits.append((i, "exclamation", line.strip()[:60]))
            if "\u2014" in line: hits.append((i, "unicode-emdash", "use --- and limit"))
            if line.strip() == "":
                if para_dashes > 1: hits.append((para_start, "dashes-in-paragraph", str(para_dashes)))
                para_dashes = 0; para_start = i + 1
            else:
                para_dashes += line.count("---")
        if END_ENV.search(line): depth = max(0, depth - 1)
    for h in hits: print(f"{path}:{h[0]}: [{h[1]}] {h[2]}")
    print(f"TOTAL HITS: {len(hits)}")
    return 1 if hits else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
