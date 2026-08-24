# Core style rules

These rules derive from the ROCm custom style instructions. They apply to all
ROCm documentation unless overridden by a more specific rule file.

**Format applicability:** ROCm documentation uses both reStructuredText (rST,
preferred for documentation pages) and Markdown (MyST, used for READMEs and
some pages). Where syntax differs between formats, examples for both are
provided. The underlying style requirement is the same regardless of format.

## Language

### Rule: CORE-001
**Severity:** error
**Scope:** All documentation — spelling
**Rule:** Use American English spelling as defined by the Merriam-Webster dictionary. See `rules/02-spelling-terminology.md` for specific terms.
**Wrong:** `colour`, `behaviour`, `organise`, `licence` (noun, in American English)
**Right:** `color`, `behavior`, `organize`, `license`
**Source:** ROCm custom

---

### Rule: CORE-002
**Severity:** error
**Scope:** All documentation — serial comma
**Rule:** Use the serial (Oxford) comma consistently in all lists of three or more items.
**Wrong:**
```md
ROCm supports HIP, OpenCL and Fortran.
```
**Right:**
```md
ROCm supports HIP, OpenCL, and Fortran.
```
**Source:** ROCm custom

---

### Rule: CORE-003
**Severity:** error
**Scope:** All documentation — slash usage
**Rule:** Use "and" or "or" instead of a slash to join alternatives or pairs.
**Wrong:**
```md
Install/configure the driver.
Use the input/output stream.
```
**Right:**
```md
Install and configure the driver.
Use the input or output stream.
```
**Exception:** Established technical terms where the slash is part of the name are acceptable (e.g., "I/O", "TCP/IP", "client/server architecture").
**Source:** ROCm custom

---

### Rule: CORE-004
**Severity:** error
**Scope:** All documentation — inclusive language
**Rule:** Avoid gendered or ableist language. Flag any non-inclusive language for removal. Use gender-neutral terms and accessible phrasing.
**Wrong:** `manpower`, `he/she`, `whitelist/blacklist`, `sanity check`, `crippled`
**Right:** `workforce`, `they`, `allowlist/denylist`, `confidence check`, `degraded`
**Source:** ROCm custom

---

### Rule: CORE-005
**Severity:** error
**Scope:** All documentation — person and voice
**Rule:** Always write in the second person singular ("you") instead of first-person plural ("we"). Prefer "you" over "the user".
**Wrong:**
```md
We recommend installing the latest driver.
The user should verify the installation.
```
**Right:**
```md
Install the latest driver.
Verify the installation.
```

```routing
tier: hybrid
applies_when: [first_person, vale:CORE-005]
strategy: lexical
pattern: (?i)\b(we|us|our|the user)\b
context_lines: 2
owner_for_detection: false
```

**Source:** ROCm custom

---

### Rule: CORE-006
**Severity:** warning
**Scope:** All documentation — tense consistency
**Rule:** Use consistent tense throughout a document. Do not switch between present and past tense without reason.

```routing
tier: llm
applies_when: ["*"]
strategy: whole_file
note: Tense consistency requires reading whole document.
```

**Source:** ROCm custom

---

## File naming

### Rule: CORE-007
**Severity:** error
**Scope:** All files — file and folder names
**Rule:** Give files descriptive, concise names in lowercase. Use dash-case (hyphens) for multi-word file and folder names. Do not use underscores, spaces, or camelCase.
**Wrong:** `Deep_Learning_ROCm.rst`, `deepLearningRocm.rst`, `Chapter1.md`
**Right:** `deep-learning-rocm.rst`
**Note:** See also META-010 for SEO-specific file naming requirements.
**Source:** ROCm custom

---

## Headings

### Rule: CORE-008
**Severity:** error
**Scope:** All documentation — heading case
**Rule:** Use sentence case for all headings. Only capitalize the first word and proper nouns.
**Wrong (Markdown):**
```md
## Getting Started With ROCm On Linux
```
**Wrong (rST):**
```rst
Getting Started With ROCm On Linux
===================================
```
**Right (Markdown):**
```md
## Getting started with ROCm on Linux
```
**Right (rST):**
```rst
Getting started with ROCm on Linux
===================================
```
**Source:** ROCm custom

---

### Rule: CORE-009
**Severity:** error
**Scope:** All documentation — stacked headings
**Rule:** Do not stack headings (a heading immediately followed by another heading with no text between them). Include explanatory text between headings.
**Wrong (Markdown):**
```md
## Installation

### Prerequisites
```
**Wrong (rST):**
```rst
Installation
============

Prerequisites
-------------
```
**Right (Markdown):**
```md
## Installation

This section describes how to install ROCm on your system.

### Prerequisites
```
**Right (rST):**
```rst
Installation
============

This section describes how to install ROCm on your system.

Prerequisites
-------------
```
**Note:** See also META-005 for SEO implications of heading structure.
**Source:** ROCm custom

---

### Rule: CORE-010
**Severity:** warning
**Scope:** All documentation — generic headings
**Rule:** Avoid generic headings such as "Introduction", "Conclusion", "References", "Acknowledgements", or "Appendices". Use descriptive, content-specific headings instead.
**Wrong:**
```md
## Introduction
```
**Right:**
```md
## ROCm installation overview
```
**Source:** ROCm custom

---

### Rule: CORE-011
**Severity:** warning
**Scope:** All documentation — content after headings
**Rule:** Follow headings with text rather than immediately with another element (list, table, or image). A brief introductory sentence provides context.
**Wrong (Markdown):**
```md
## Supported operating systems

| OS | Version |
|----|---------|
| Ubuntu | 22.04 |
```
**Wrong (rST):**
```rst
Supported operating systems
===========================

.. list-table::

   * - OS
     - Version
   * - Ubuntu
     - 22.04
```
**Right (Markdown):**
```md
## Supported operating systems

ROCm supports the following operating systems.

| OS | Version |
|----|---------|
| Ubuntu | 22.04 |
```
**Right (rST):**
```rst
Supported operating systems
===========================

ROCm supports the following operating systems.

.. list-table::

   * - OS
     - Version
   * - Ubuntu
     - 22.04
```
**Source:** ROCm custom

---

## Links

### Rule: CORE-012
**Severity:** error
**Scope:** All documentation — link anchor text
**Rule:** Use meaningful, descriptive link anchors. Do not use generic text like "here", "this document", "click here", or "link".
**Wrong (Markdown):**
```md
For more information, see [here](./install.md).
```
**Wrong (rST):**
```rst
For more information, see `here <install.rst>`_.
```
**Right (Markdown):**
```md
For more information, see [Installing ROCm](./install.md).
```
**Right (rST):**
```rst
For more information, see :doc:`Installing ROCm <install>`.
```
**Note:** See also META-016 for SEO implications of link text.
**Source:** ROCm custom

---

## Acronyms

### Rule: CORE-013
**Severity:** warning
**Scope:** All documentation — acronym definitions
**Rule:** Spell out and define acronyms on first use, except for well-known acronyms (e.g., API, GPU, CPU, RAM, OS, URL, HTML, SDK, AI, RCCL, SQTT, CI, ROCR, HSA, SIMD, ISA, SMI, MPICH, CLI, APU, VRAM, PID, GEMM, LLM, OEM, GPT) and the following terms, which are treated as proper names and do not require expansion: ROCm, HIP, CDNA, RDNA, GCN, JAX, AMDGPU, EPYC, SUSE. MAX and PRO are also exempt, but only when they appear as Ryzen AI product-name components (e.g., "Ryzen AI MAX+ PRO 395") — not as standalone words. Format: "Full Name (ACRONYM)".
**Wrong:**
```md
Use the VA-API to decode video streams.
```
**Right:**
```md
Use the Video Acceleration API (VA-API) to decode video streams.
```

```routing
tier: hybrid
applies_when: [uncommon_acronyms]
strategy: lexical
context_lines: 3
note: Script-half finds candidate acronyms; LLM judges first-use expansion.
```

**Source:** ROCm custom

---

### Rule: CORE-018
**Severity:** suggestion
**Scope:** All documentation — acronym spell-out
**Rule:** Flag three-to-five-letter, all-caps tokens that appear without an accompanying "Full Name (ACRONYM)" spell-out nearby, so authors can add one if the acronym isn't widely known. Exempt well-known general acronyms (API, GPU, CPU, HTML, URL, etc.) and AMD/ROCm proper-name acronyms that are never spelled out in ROCm docs: AMD, SMI, LLVM, APU, SIMD, VRAM, CUDA, HIP, CDNA, RDNA, GCN, GEMM.
**Wrong:**
```md
Use the VA-API to decode video streams.
```
**Right:**
```md
Use the Video Acceleration API (VA-API) to decode video streams.
```

**Also right (exempt acronyms, no spell-out needed):**
```md
Check GPU utilization with the AMD SMI tool.
```

**Note:** Unlike CORE-013 (which judges whether a *first use* was properly expanded), CORE-018 is a pure lexical check for the mere presence of an unexpanded acronym anywhere in the text.
**Source:** ROCm custom (supersedes Google.Acronyms)

---

## Technical terms

### Rule: CORE-014
**Severity:** warning
**Scope:** All documentation — term consistency
**Rule:** If multiple terms or spellings exist for the same concept, pick one and use it consistently throughout the document and across the documentation set. See `wordlists/preferred-terms.yml` for standardized terminology.
**Wrong:** Using "GPU kernel" in one paragraph and "device kernel" in the next when referring to the same concept.
**Right:** Pick one term and use it throughout.

```routing
tier: llm
applies_when: ["*"]
strategy: whole_file
note: Same-concept term drift -- cross-passage semantic consistency.
```

**Source:** ROCm custom

---

## Images

### Rule: CORE-015
**Severity:** error
**Scope:** All documentation — image alt text
**Rule:** Include alt text for all images. Do not start alt text with "this is an image of" or similar phrasing. Describe the content directly.
**Wrong (Markdown):**
```md
![This is an image of the ROCm architecture](./rocm-arch.png)
```
**Wrong (rST):**
```rst
.. image:: ./rocm-arch.png
   :alt: This is an image of the ROCm architecture
```
**Right (Markdown):**
```md
![ROCm software stack architecture showing the kernel driver, runtime, and library layers](./rocm-arch.png)
```
**Right (rST):**
```rst
.. image:: ./rocm-arch.png
   :alt: ROCm software stack architecture showing the kernel driver, runtime, and library layers
```
**Note:** See also META-008 for SEO-specific alt text requirements.

```routing
tier: hybrid
applies_when: [has_image]
strategy: structural
section_scope: true
note: Vale/Script confirm alt-text presence; LLM judges descriptiveness.
```

**Source:** ROCm custom

---

### Rule: CORE-016
**Severity:** warning
**Scope:** All documentation — image attribution
**Rule:** Provide attributions and credits for images where applicable, especially for third-party images.

```routing
tier: llm
applies_when: [has_image]
strategy: structural
section_scope: true
note: Third-party image attribution -- needs provenance judgment.
```

**Source:** ROCm custom

---

## Tables

### Rule: CORE-017
**Severity:** warning
**Scope:** All documentation — table alignment
**Rule:** Left-align all text in tables.
**Wrong (Markdown):**
```md
| Feature | Status |
|:-------:|:------:|
| HIP | Supported |
```
**Wrong (rST):**
```rst
.. list-table::
   :align: center

   * - Feature
     - Status
   * - HIP
     - Supported
```
**Right (Markdown):**
```md
| Feature | Status |
|---------|--------|
| HIP | Supported |
```
**Right (rST):**
```rst
.. list-table::

   * - Feature
     - Status
   * - HIP
     - Supported
```
**Note:** rST `list-table` and `csv-table` directives left-align by default. Markdown pipe tables left-align by default (no `:` alignment markers needed).
**Source:** ROCm custom

---

## Units

### Rule: CORE-020
**Severity:** error
**Scope:** All documentation — units of measure
**Rule:** Following Google style, put a nonbreaking space between a number and its unit of measure (bytes, metric-prefixed bytes, time units). Don't flag a bare digit-plus-"B" run when it's part of an LLM model name's parameter-count suffix rather than a byte count — specifically when the digits are hyphen-joined to the model name, or preceded by another bare number (a version number) and a space.
**Wrong:**
```md
The file is 20GB.
```
**Right:**
```md
The file is 20 GB.
```

**Also right (LLM model name, not a byte count):**
```md
GPT-OSS-20B and Llama 3 405B are both supported.
```
**Note:** Model names written as "Name NNNB" with no hyphen and no version number in between (e.g., "Llama 70B") are still flagged; narrowing the exclusion further risks swallowing genuine byte-count typos.
**Source:** ROCm custom (supersedes Google.Units)

---

## Version numbers

### Rule: CORE-021
**Severity:** warning
**Scope:** All documentation — version-number placeholders
**Rule:** When documentation uses placeholder letters in place of a real ROCm version number (for example, in generic installation instructions or command examples), write those placeholder letters in lowercase. Never use uppercase letters for version-number placeholders.
**Wrong:**
```md
Install ROCm 7.X.Y using your package manager.
Download rocm-7.X from the repository.
```
**Wrong (rST):**
```rst
Install ROCm 7.X.Y using your package manager.
```
**Right:**
```md
Install ROCm 7.x.y using your package manager.
Download rocm-7.x from the repository.
```
**Right (rST):**
```rst
Install ROCm 7.x.y using your package manager.
```
**Note:** Implemented in Vale as `vale/styles/ROCm/CORE-021.yml`, an `existence` rule matching a digit run followed by a literal dot and an uppercase letter, optionally repeated for additional dot-separated components (so it catches both two-component placeholders like `7.X` and three-component placeholders like `7.X.Y` or `12.A.B`). Requiring a literal dot immediately before the uppercase letter means the rule does not fire on product names that place digits directly against an uppercase letter with no dot in between, such as `MI300X` or `MI300A`. It also does not fire on real version numbers such as `7.0.1` (digits, not uppercase letters, follow the dot) or on correctly-formatted lowercase placeholders such as `7.x.y`.
**Source:** ROCm custom

---

### Rule: CORE-022
**Severity:** warning
**Scope:** All documentation — version number formatting
**Rule:** Do not use a `v` prefix before a version string in documentation as it's redundant.
**Wrong:**
```md
Install ROCm v7.14.0 using your package manager.
ROCm v5.7 is no longer supported.
CUDA v12.0 is required.
```
**Right:**
```md
Install ROCm 7.14.0 using your package manager.
ROCm 5.7 is no longer supported.
CUDA 12.0 is required.
```
**Note:** Implemented in Vale as `vale/styles/ROCm/CORE-022.yml`, an `existence` rule matching a standalone `v` (with an optional dot and optional space) immediately preceding a digit sequence, such as `v7.14`, `v.7.14`, or `v 7.14`.
**Source:** ROCm custom

---

## Description lists

### Rule: CORE-023
**Severity:** warning
**Scope:** All documentation — description-list entry formatting
**Rule:** When a description list is presented as a run of "**Term:** Description" entries (for example, in a bulleted list), each entry's formatting must follow one convention: the term is bold, the colon falls inside the bold markers immediately after the term (`**Term:**`, not `**Term**:` or `**Term** :`), with no space between the term and the colon, and exactly one space between the closing `**` and the description.
**Wrong:**
```md
- **Optimization**: Enables aggressive compiler optimizations.
- **Debug :**Includes debug symbols for troubleshooting.
- **Verbose:**  Prints extra diagnostic output.
```
**Right:**
```md
- **Optimization:** Enables aggressive compiler optimizations.
- **Debug:** Includes debug symbols for troubleshooting.
- **Verbose:** Prints extra diagnostic output.
```
(The same convention applies in rST: rST inline strong emphasis also uses `**text**`, so the wrong/right forms above are unchanged.)
**Note:** CORE-019 (a general colon-capitalization rule) has been removed — it enforced guidance the current ROCm style guide no longer states, and directly contradicted the guide's "Description lists" section, which requires capitalizing the first word of each description. Implemented in Vale as `vale/styles/ROCm/CORE-023.yml`, an `existence` rule matching the malformed bold-term/colon patterns.
**Source:** ROCm custom
