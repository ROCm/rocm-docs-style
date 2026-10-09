<!--
Regression fixture for SPELL-003: the product-name casing swaps must only fire
on a standalone miscased name, not on a substring of a longer identifier, a
kebab-case slug, an environment variable, a path segment, or a URL. Run:
`vale --config=vale/.vale.ini vale/testdata/spell-003-boundaries.md`

Expected ROCm.SPELL-003 findings: exactly 3, all in the final section
(one each on the `rocm 6.0`, `migraphx` and `hipblas` lines). The identifier
section must produce none. Before the fix, `HIPBLASLt` and `migraphx-driver`
and `ROCM_PATH` all fired because only the ROCm key had a boundary guard.
-->

# SPELL-003 boundaries

Identifiers, slugs, paths and URLs (no SPELL-003 findings expected):

Use HIPBLASLt for GEMM, or run the migraphx-driver tool.

Set ROCM_PATH and MIGRAPHX_SET_GEMM_PROVIDER before launching.

Packages live in the rocm/ directory of the repository.

Clone https://github.com/ROCm/rocm-examples and read https://example.com/rocm/docs for details.

Genuine miscasing (one SPELL-003 finding per line):

Tested with rocm 6.0 on Linux.

Build migraphx from source.

Install hipblas before continuing.
