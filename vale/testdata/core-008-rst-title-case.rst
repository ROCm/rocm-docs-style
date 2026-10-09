..
   Counterpart to core-008-rst-acronyms.rst: genuine Title Case headings MUST
   still be flagged by ROCm.CORE-008 on reStructuredText after the
   acronym/camelCase fix. Run:
   `vale --config=vale/.vale.ini vale/testdata/core-008-rst-title-case.rst`

   Expected: exactly 5 ROCm.CORE-008 findings, one per heading below (the
   `capitalization` check reports once per heading, not once per word).

   "Resolved Issues" and "Step 5: Test MIOpen Components" are regressions found
   on real documentation: a word that appears in a listed multi-word name
   ("GitHub Issues", "ROCm Bandwidth Test") must not be exempt everywhere.

Getting started with ROCm
=========================

Configuring Network Settings
============================

Getting Started With ROCm On Linux
==================================

Installing The ROCm Driver Package
==================================

Resolved Issues
===============

Step 5: Test MIOpen Components
==============================
