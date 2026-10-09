<!--
Regression fixture for CORE-003: a slash that is part of a file or URL path is
not an "and"/"or" alternative. Run:
`vale --config=vale/.vale.ini vale/testdata/core-003-paths.md`

Expected ROCm.CORE-003 findings: exactly 7, all in the final section (one per
line, except `apt/dnf/zypper`, which yields one finding for its first pair).
The path section must produce none. Before the fix, the path "data/components"
inside "/data/components-current.yaml" and "docs/index" inside "docs/index.rst"
both fired.

The genuine-alternative lines include chains and hyphenated second words
("apt/dnf/zypper", "peer/host-memory", "find/perf-database"). An earlier
version of the path guard swallowed those; they must keep firing.

Not tested, known limitation: a relative path with no leading slash and no
extension ("usr/bin/env") is structurally identical to "apt/dnf/zypper" and
is flagged.
-->

# CORE-003 paths

Paths and filenames (no CORE-003 findings expected):

Edit the file /data/components-current.yaml before building.

Open docs/index.rst and then docs/reference/api.md for details.

Install from pytorch.org/get-started/locally on any host.

Set the page to docs/system-optimization/index.rst for now.

Write the output under data/reference/gpu-atomics-operation/ first.

Genuine alternatives (one CORE-003 finding per line):

Run the install/configure step first.

Choose read/write access for the mount.

Pass the input/output buffers.

Use apt/dnf/zypper to install the package.

Check peer/host-memory transfers.

Run find/perf-database before profiling.

Then verify the build/deploy order.
