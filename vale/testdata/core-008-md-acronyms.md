<!--
Regression fixture for CORE-008-MD: all-caps acronyms, camelCase tool names,
GPU model names, and listed proper nouns in ATX headings are NOT title-case
violations. Run:
`vale --config=vale/.vale.ini vale/testdata/core-008-md-acronyms.md`

Expected: zero ROCm.CORE-008-MD findings. Before the fix, the rule flagged any
token starting with a capital that was not in its exception list, so
`XGBoost`, `CMake`, `WebUI`, `MI300X`, `(PC)`, `RDMA`, `NIC` and `MoRI` all
fired even though none of them is a Capitalized-Word (capital + lowercase
only) style violation.

The counterpart that MUST still fire is core-008-md-title-case.md.
-->

# Getting started with ROCm

## Using XGBoost and CMake with the WebUI

## Support for MI300X and MI350 GPUs

### Program counter (PC) sampling

## Deploying with Docker and Ollama on GitHub

## Release notes for the August update

## AMD GPU Driver release notes

## RDMA and NIC configuration with MoRI

## Running Dask on ROCm

## Support for Strix Halo and Krackan Point

## Using Visual Studio Code with GitHub Issues
