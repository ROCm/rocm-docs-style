..
   Regression fixture for CORE-003 on reStructuredText: slashes that belong to
   a path inside a directive body or an indented shell block are not "and"/"or"
   alternatives. Run:
   `vale --config=vale/.vale.ini vale/testdata/core-003-rst-directives.rst`

   Expected ROCm.CORE-003 findings: exactly 1, on the final prose line
   ("install/configure"). Before the fix, the path inside the directive body
   ("data/components") and the paths inside the shell block ("opt/rocm",
   "rocm/bin") each produced findings. Both constructs are taken from real
   ROCm and AMDMIGraphX documentation.

CORE-003 directives
===================

.. datatemplate:yaml:: /data/components-current.yaml

    {%- set defaults = load("/data/components-default.yaml").components -%}

Option: op
**********

   $ /opt/rocm/bin/migraphx-driver op --list

Run the install/configure step first.
