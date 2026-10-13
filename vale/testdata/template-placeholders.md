<!--
Regression fixture for template placeholders: Sphinx, MyST and Jinja
substitutions such as `{{ ROCM_VERSION }}` and `{% if flag %}` are markup, not
prose, so they are ignored by every check (TokenIgnores in vale/.vale.ini). Run:
`vale --config=vale/.vale.ini vale/testdata/template-placeholders.md`

Expected ROCm.SPELL-003 findings: exactly 1, on the final line ("Rocm", outside
any placeholder). Everything inside {{ ... }} and {% ... %} must produce none.
Before the change, `{{ rocm }}` and `{% if rocm %}` fired, because the bare
word "rocm" inside a placeholder was read as prose.
-->

# Template placeholders

Install ROCm {{ ROCM_VERSION }} on the host.

Install ROCm {{ rocm_version }} on the host.

Install the {{ rocm }} package on the host.

{% if flag %}Enable the flag.{% endif %}

{% if rocm %}Use the ROCm build.{% endif %}

Install Rocm on the host.
