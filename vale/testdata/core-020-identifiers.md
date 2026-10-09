<!--
Regression fixture for CORE-020: unit-of-measure tokens must not match inside
file names, identifiers, or decimal LLM parameter counts, and the rule is now
warning level (house style, not a build-breaker). Run:
`vale --config=vale/.vale.ini vale/testdata/core-020-identifiers.md`

Expected ROCm.CORE-020 findings: exactly 3 (20GB, 50ms, 5min), all in the final
section, and all at WARNING level. The identifier section must produce none.
Before the fix `2d_regression` fired as "2d" days and "2.7B" / "6.7B" fired as
bare "7B" byte counts, and every finding was error level.

Known limitation, not tested: "0s" and "1s" meaning zeros and ones are
indistinguishable from seconds and still fire.
-->

# CORE-020 identifiers

Identifiers and parameter counts (no CORE-020 findings expected):

See the 2d_regression/image_restoration.ipynb tutorial and the 3d_segmentation notebook.

The OPT-1.3B model has 2.7B and 6.7B variants.

Real units missing a space (one CORE-020 finding per line):

Allocate 20GB of memory.

Wait 50ms for completion.

Allow 5min for the build.
