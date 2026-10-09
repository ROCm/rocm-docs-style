<!--
Counterpart to core-008-md-acronyms.md: genuine Title Case headings MUST still
be flagged by ROCm.CORE-008-MD after the acronym/camelCase fix. Run:
`vale --config=vale/.vale.ini vale/testdata/core-008-md-title-case.md`

Expected ROCm.CORE-008-MD findings (the heading's first word is always exempt):
  line 15: "Network", "Settings"    -> 2
  line 17: "The", "Package"         -> 2   ("ROCm" and "Driver" are exempt)
  line 19: "Started", "With", "On"  -> 3   ("ROCm" and "Linux" are exempt)
  line 21: "Issues"                 -> 1   (exempt only after "GitHub", not here)
  line 23: "Test", "Components"     -> 2   (exempt "Test" only inside "ROCm Bandwidth Test")
Total: 10.

The last two lines are regressions found on real documentation: exempting a
word because it appears in a listed multi-word name must not exempt that word
everywhere. "Resolved Issues" and "Step 5: Test MIOpen Components" were both
wrongly passed by an earlier word-by-word version.
-->

# Getting started with ROCm

## Configuring Network Settings

## Installing The ROCm Driver Package

## Getting Started With ROCm On Linux

## Resolved Issues

## Step 5: Test MIOpen Components
