<!--
Regression fixture for word-choice rule overlap and conflicts. Run:
`vale --config=vale/.vale.ini vale/testdata/word-choice-dedupe.md`

Expected findings: exactly 3 in total (anything else from these lines is a regression):
  open-source line   -> 0                               (was 2: CORE-024 + Google.WordListCase;
                                                         the swap was then removed, SPELL-006 defers it)
  in order to line   -> exactly 1: ROCm.CORE-024        (was 2-3: + SPELL-009, WordListCase)
  backend line       -> 0                               (was 1 error: Microsoft.Avoid)
  CLI line           -> 0                               (was 1: CORE-024 CLI swap)
  silently line      -> 0                               (was 2: Microsoft.Adverbs)
  will line          -> 0                               (was 1: Google.Will)
  very line          -> exactly 1: ROCm.CORE-026
  and so on line     -> exactly 1: ROCm.CORE-025

`backend` is the PREFERRED ROCm spelling (rules/02-spelling-terminology.md,
wordlists/preferred-terms.yml); Microsoft.Avoid contradicted ratified policy
and at error level.
-->

# Word choice overlap

This plugin is open-source and supported.

Cache the result in order to speed up later runs.

The compiler backend generates the code.

Use the ROCm CLI to list devices.

The kernel silently drops requests and samples randomly.

The patch will fix the crash in a later release.

The result is very fast.

Install, configure, and so on.
