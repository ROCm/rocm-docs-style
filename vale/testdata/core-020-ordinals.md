<!--
Regression fixture for CORE-020: the unit-of-measure tokens must not match the
leading characters of an unrelated word. Run:
`vale --config=vale/.vale.ini vale/testdata/core-020-ordinals.md`

Expected ROCm.CORE-020 findings: exactly 3 (50ms, 20GB, 5min), all in the
final section. The ordinal section must produce none (Google.Ordinal may
still fire there; that is a separate rule). Before the fix, the bare `s`
unit matched the "1s" inside "1st" and the "21s" inside "21st", producing a
CORE-020 alert on top of every Google.Ordinal alert.

Known limitation, intentionally not tested: "0s" and "1s" meaning zeros and
ones are indistinguishable from seconds and still fire.
-->

# CORE-020 boundaries

Ordinals (no CORE-020 findings expected):

This is the 1st item, the 21st item, and the 31st item.

Real units missing a space (one CORE-020 finding per line):

Wait 50ms for completion.

Allocate 20GB of memory.

Allow 5min for the build.
