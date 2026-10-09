..
   Regression fixture for CORE-008 on reStructuredText: all-caps acronyms,
   camelCase tool names, GPU model numbers, and listed proper nouns in
   headings are NOT title-case violations. Run:
   `vale --config=vale/.vale.ini vale/testdata/core-008-rst-acronyms.rst`

   Expected: zero ROCm.CORE-008 findings. Before the fix, `capitalization`
   flagged the whole heading whenever it held a word like `XGBoost`, `CMake`,
   `MI300X`, `(PC)` or `MoRI`, because only a fixed list of names was exempt.

   Headings that start with a lowercase letter (`dynamic_dimension`,
   `parse_onnx`, `migraphx::program`) are API identifiers, not sentences, and
   are exempt too. This also means a heading that merely forgets to capitalize
   its first word is not caught by the rule; that is left to the review tier.

   The counterpart that MUST still fire is core-008-rst-title-case.rst.

Getting started with ROCm
=========================

Using XGBoost and CMake with the WebUI
======================================

Support for MI300X and MI350 GPUs
=================================

Program counter (PC) sampling
=============================

Deploying with Docker and Ollama on GitHub
==========================================

Release notes for the August update
===================================

AMD GPU Driver release notes
============================

RDMA and NIC configuration with MoRI
====================================

ROCm Core SDK
=============

ROCm Data Center
================

ROCm Compute Profiler
=====================

Composable Kernel
=================

dynamic_dimension
=================

parse_onnx
==========

migraphx::program
=================

Support for Strix Halo and Krackan Point
========================================

Using Visual Studio Code with GitHub Issues
===========================================
