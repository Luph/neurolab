# Excel function availability by version (Microsoft 365, Excel 2021, Excel 2024): XLOOKUP, LET, LAMBDA, dynamic arrays and related functions

As of: 2026-10-03 (Microsoft Support "Applies To" lists and product pages reviewed on 3 October 2026; latest lifecycle event: Office 2021 retirement on 13 October 2026)

## Summary

Which modern Excel functions a model can use depends on the version its users run. Microsoft's support pages show the following:
- Dynamic arrays (spilling formulas and the functions FILTER, SORT, SORTBY, UNIQUE, SEQUENCE and RANDARRAY), XLOOKUP, XMATCH and LET are available in Excel for Microsoft 365, Excel 2021 and Excel 2024.
- LAMBDA and its helper functions (MAP, BYROW and others) are in Microsoft 365 and Excel 2024 but not Excel 2021.
- The 14 newer text and array functions (TEXTSPLIT, VSTACK, TAKE and others) are also in Microsoft 365 and Excel 2024 only.
- GROUPBY and TRIMRANGE are listed for Microsoft 365 only. The REGEX functions are listed for Microsoft 365 for Windows and Mac only.
- XLOOKUP is not available in Excel 2016 or Excel 2019.

Office 2016 and 2019 reached end of extended support in October 2025. Office 2021 retires on 13 October 2026. Office 2024 is supported until 9 October 2029.

For a project finance model that will be shared with lenders, advisers and auditors, the practical baseline in late 2026 is Excel 2021 functionality (XLOOKUP, LET, dynamic arrays). LAMBDA and the newer array functions are safe only if every counterparty is on Microsoft 365 or Excel 2024.

## Verified facts

1. XLOOKUP: the Microsoft Support page states: "XLOOKUP is not available in Excel 2016 and Excel 2019." The page notes that users of those versions may still open workbooks containing XLOOKUP created in newer versions. (The page's "Applies To" banner nonetheless lists Excel 2019 and 2016, so rely on the body text.) "What's new in Excel 2021" lists XLOOKUP as a new feature of Excel 2021. [confidence: high] [source: 1, 6]
2. LET: Applies To lists Excel for Microsoft 365 (Windows and Mac), Excel 2024 (Windows and Mac) and Excel 2021 (Windows and Mac). "What's new in Excel 2021" lists LET as new in Excel 2021. [confidence: high] [source: 2, 6]
3. LAMBDA: Applies To lists Excel for Microsoft 365 (Windows and Mac) and Excel 2024 (Windows and Mac), not Excel 2021. "What's new in Excel 2024" states that "The LAMBDA function has been added to Excel 2024 and Excel 2024 for Mac". The LAMBDA helper functions MAP and BYROW have the same Applies To list (Microsoft 365 and 2024). [confidence: high] [source: 3, 7, 9]
4. Dynamic arrays: according to Microsoft, dynamic array formulas were introduced in September 2018, and "Dynamic array formula support was released to Microsoft 365 subscribers in Current Channel in January 2020." "What's new in Excel 2021" lists dynamic arrays with six new functions (FILTER, SORT, SORTBY, UNIQUE, SEQUENCE, RANDARRAY), plus XMATCH, as new in Excel 2021. The Applies To lists for FILTER, SORT, UNIQUE, SEQUENCE and XMATCH include Microsoft 365, 2024 and 2021. [confidence: high] [source: 4, 6, 9]
5. Legacy array formulas entered with Ctrl+Shift+Enter (CSE) "are still supported for back compatibility reasons, but should no longer be used", according to Microsoft. When a dynamic array formula is opened in an older, non-dynamic-aware version, it appears as a legacy CSE formula. Dynamic-array Excel also introduced the implicit intersection operator (@), which can appear in older formulas when they are opened in new Excel. [confidence: high] [source: 4, 5]
6. Excel 2024 new features ("What's new in Excel 2024 for Windows and Mac"):
- 14 new text and array functions;
- the LAMBDA function;
- the IMAGE function;
- dynamic arrays referenced in charts;
- XLL add-ins from the internet blocked by default;
- an Accessibility ribbon;
- OpenDocument Format 1.4 support;
- performance improvements.

Unless otherwise noted, these features are in both Excel 2024 and Excel LTSC 2024. [confidence: high] [source: 7]
7. Applies To lists for the 14 text and array functions, checked for TEXTSPLIT, VSTACK and TAKE: Microsoft 365 (Windows and Mac) and Excel 2024 (Windows and Mac). IMAGE also lists Microsoft 365, Excel 2024 and some mobile apps. [confidence: high for functions checked] [source: 9]
8. Applies To lists for functions available only in Microsoft 365: GROUPBY and TRIMRANGE list "Excel for Microsoft 365" only. REGEXTEST lists Microsoft 365 for Windows and Mac only. [confidence: medium (Applies To banners can be inaccurate; see item 1)] [source: 9]
9. Functions available since Excel 2019: IFS, MAXIFS and TEXTJOIN list Excel 2019 and later (2021, 2024, Microsoft 365). [confidence: high] [source: 9]
10. Excel 2021 versus Excel LTSC 2021: some Excel 2021 features are not in Excel LTSC 2021 for commercial customers, including co-authoring, modern comments, sheet views and the visual refresh. XLOOKUP, LET, dynamic arrays and XMATCH are not flagged as excluded. [confidence: high] [source: 6]
11. Support lifecycle (Microsoft Learn; Microsoft shows times in UTC):
- Office 2016: extended support ended on 14 October 2025 (shown as 15 October 2025, 06:59:59 UTC).
- Office 2019: extended support ended on the same date.
- Office 2021: retirement on 13 October 2026 (shown as 14 October 2026, 06:59:59 UTC).
- Office 2024: started 1 October 2024; retirement on 9 October 2029 (shown as 10 October 2029, 06:59:59 UTC).

[confidence: high] [source: 8]
12. Office LTSC 2024 "doesn't include the latest cloud-backed features and functionality" available in Microsoft 365 subscriptions, according to Microsoft's LTSC 2024 overview. [confidence: high] [source: 10]

Availability matrix (from items 1–9; "Y" = listed by Microsoft)

| Function or feature | Microsoft 365 | Excel 2024 | Excel 2021 | Excel 2019 |
|---|---|---|---|---|
| IFS, MAXIFS, TEXTJOIN | Y | Y | Y | Y |
| XLOOKUP | Y | Y | Y | No (stated in body text) |
| XMATCH | Y | Y | Y | Not listed |
| Dynamic arrays; FILTER, SORT, UNIQUE, SEQUENCE | Y | Y | Y | No spill (legacy CSE) |
| LET | Y | Y | Y | Not listed |
| LAMBDA, MAP, BYROW | Y | Y | Not listed | Not listed |
| TEXTSPLIT, VSTACK, TAKE (14 text/array functions) | Y | Y | Not listed | Not listed |
| IMAGE | Y | Y | Not listed | Not listed |
| GROUPBY, TRIMRANGE | Y | Not listed | Not listed | Not listed |
| REGEXTEST | Y | Not listed | Not listed | Not listed |

## Timeline

- 22 September 2015: Office 2016 support start.
- 24 September 2018: Office 2019 support start.
- September 2018: Dynamic array formulas introduced (Microsoft's wording).
- January 2020: Dynamic arrays released to Microsoft 365 Current Channel.
- 5 October 2021: Office 2021 support start (XLOOKUP, LET, dynamic arrays in a perpetual version).
- 1 October 2024: Office 2024 support start (adds LAMBDA and the 14 text/array functions to a perpetual version).
- 14 October 2025: Office 2016 and Office 2019 end of extended support.
- 13 October 2026: Office 2021 retirement.
- 9 October 2029: Office 2024 retirement.

## Financing and structure details

Not applicable. For model governance: lenders' model auditors, technical advisers and borrowers often run different Excel builds, so a model's term sheet or modelling protocol should specify the minimum Excel version.

## What went wrong or right, and why

- Microsoft's Applies To banners are not always consistent with page bodies. The XLOOKUP banner lists Excel 2016 and 2019, while the body says XLOOKUP is not available in those versions. Writers should cite body text or the "What's new" pages where possible. [source: 1]

## Teaching angles by chapter

- Ch 13 (Excel for project finance): Teach INDEX/MATCH as the universal baseline and XLOOKUP as the preferred lookup where every user has Excel 2021 or later (exact match by default, a built-in if-not-found argument, no column index to break). Teach LET for readability in long formulas such as CFADS or sculpting. Treat LAMBDA and dynamic-array-heavy designs as an advanced option, because Excel 2021 lacks LAMBDA and spilled ranges can complicate fixed-row layouts and audit tools. Recommend a "version policy" line in the model's cover sheet. Note that Office 2021 support ends on 13 October 2026, which narrows the installed base to Microsoft 365 and 2024 over time, and that CSE array formulas should not be used in new models.

## Do not state

- That XLOOKUP works in Excel 2019 or 2016. Microsoft says it does not.
- That LAMBDA is in Excel 2021. It is not listed, and Microsoft describes it as added in Excel 2024.
- That PIVOTBY is available in Excel 2021 or 2024. Its Applies To banner lists them, but this conflicts with GROUPBY (Microsoft 365 only) and was not confirmed in body text. Treat PIVOTBY and GROUPBY as Microsoft 365 only unless verified.
- Release dates for XLOOKUP general availability in Microsoft 365, or for the COPILOT function. Neither was verified in this session (the COPILOT function page returned an error).
- That Excel for the web supports a given function, unless its Applies To list says so.

## Sources

1. Microsoft Support, "XLOOKUP function", accessed 3 October 2026, https://support.microsoft.com/en-us/office/xlookup-function-b7fd680e-6d10-43e6-84f9-88eae8bf5929
2. Microsoft Support, "LET function", accessed 3 October 2026, https://support.microsoft.com/en-us/office/let-function-34842dd8-b92b-4d3f-b325-b8b8f9908999
3. Microsoft Support, "LAMBDA function", accessed 3 October 2026, https://support.microsoft.com/en-us/office/lambda-function-bd212d27-1cd1-4321-a34a-ccbf254b8b67
4. Microsoft Support, "Dynamic array formulas in non-dynamic aware Excel" and "Dynamic array formulas and spilled array behavior", accessed 3 October 2026, https://support.microsoft.com/en-us/office/dynamic-array-formulas-in-non-dynamic-aware-excel-696e164e-306b-4282-ae9d-aa88f5502fa2 and https://support.microsoft.com/en-us/office/dynamic-array-formulas-and-spilled-array-behavior-205c6b06-03ba-4151-89a1-87a7eb36e531
5. Microsoft Support, "Implicit intersection operator: @", accessed 3 October 2026, https://support.microsoft.com/en-us/office/implicit-intersection-operator-ce3be07b-0101-4450-a24e-c1c999be2b34
6. Microsoft Support, "What's new in Excel 2021 for Windows", accessed 3 October 2026, https://support.microsoft.com/office/f953fe71-8f85-4423-bef9-8a195c7a1100
7. Microsoft Support, "What's new in Excel 2024 for Windows and Mac", accessed 3 October 2026, https://support.microsoft.com/office/faee26b6-ad74-40a8-9304-aa6db716553f
8. Microsoft Learn, Lifecycle pages: "Office 2021", "Office 2024", "Microsoft Office 2019", "Microsoft Office 2016", accessed 3 October 2026, https://learn.microsoft.com/en-us/lifecycle/products/office-2021 ; https://learn.microsoft.com/en-us/lifecycle/products/office-2024 ; https://learn.microsoft.com/en-us/lifecycle/products/microsoft-office-2019 ; https://learn.microsoft.com/en-us/lifecycle/products/microsoft-office-2016
9. Microsoft Support function pages (Applies To lists), accessed 3 October 2026: FILTER https://support.microsoft.com/en-us/office/filter-function-f4f7cb66-82eb-4767-8f7c-4877ad80c759 ; SORT https://support.microsoft.com/en-us/office/sort-function-22f63bd0-ccc8-492f-953d-c20e8e44b86c ; UNIQUE https://support.microsoft.com/en-us/office/unique-function-c5ab87fd-30a3-4ce9-9d1a-40204fb85e1e ; SEQUENCE https://support.microsoft.com/en-us/office/sequence-function-57467a98-57e0-4817-9f14-2eb78519ca90 ; XMATCH https://support.microsoft.com/en-us/office/xmatch-function-d966da31-7a6b-4a13-a1c6-5a33ed6a0312 ; MAP https://support.microsoft.com/en-us/office/map-function-48006093-f97c-47c1-bfcc-749263bb1f01 ; BYROW https://support.microsoft.com/en-us/office/byrow-function-2e04c677-78c8-4e6b-8c10-a4602f2602bb ; TEXTSPLIT https://support.microsoft.com/en-us/office/textsplit-function-b1ca414e-4c21-4ca0-b1b7-bdecace8a6e7 ; VSTACK https://support.microsoft.com/en-us/office/vstack-function-a4b86897-be0f-48fc-adca-fcc10d795a9c ; TAKE https://support.microsoft.com/en-us/office/take-function-25382ff1-5da1-4f78-ab43-f33bd2e4e003 ; IMAGE https://support.microsoft.com/en-us/office/image-function-7e112975-5e52-4f2a-b9da-1d913d51f5d5 ; GROUPBY https://support.microsoft.com/en-us/office/groupby-function-5e08ae8c-6800-4b72-b623-c41773611505 ; TRIMRANGE https://support.microsoft.com/en-us/office/trimrange-function-d7812248-3bc5-4c6b-901c-1afa9564f999 ; REGEXTEST https://support.microsoft.com/en-us/office/regextest-function-7d38200b-5e5c-4196-b4e6-9bff73afbd31 ; IFS https://support.microsoft.com/en-us/office/ifs-function-36329a26-37b2-467c-972b-4a39bd951d45 ; MAXIFS https://support.microsoft.com/en-us/office/maxifs-function-dfd611e6-da2c-488a-919b-9b6376b28883 ; TEXTJOIN https://support.microsoft.com/en-us/office/textjoin-function-357b449a-ec91-49d0-80c3-0e8fc845691c
10. Microsoft Learn, "Overview of Office LTSC 2024", accessed 3 October 2026, https://learn.microsoft.com/en-us/office/ltsc/2024/overview
