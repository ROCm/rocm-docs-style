# Best practices for ROCm library documentation

These rules apply to all ROCm library documentation.

---

## Format requirements

### Rule: BEST-001
**Severity:** error
**Scope:** All documentation pages — format
**Rule:** All new content introduced to the ROCm documentation set must be in reStructuredText (rST) format. Existing Markdown content must be converted to rST. Markdown is only used for repository root files (README.md, LICENSE.md, CHANGELOG.md) that are intended to be read directly in the GitHub interface.
**Source:** ROCm best practices

---

### Rule: BEST-002
**Severity:** error
**Scope:** Markdown files — manual section numbering
**Rule:** Do not number headings manually. Sphinx generates section numbers automatically. Manual numbering creates maintenance burden and causes conflicts with Sphinx's numbering.
**Wrong:**
```md
## 1. Installation
## 2. Configuration
## 3. Usage
```
**Right:**
```md
## Installation
## Configuration
## Usage
```
**Source:** ROCm best practices

---

### Rule: BEST-003
**Severity:** error
**Scope:** All documentation — heading formatting
**Rule:** Do not apply formatting such as bolding or underlines to headings. Italics may be used for a single word in a heading if appropriate. Heading styles and formats are centrally controlled via CSS.
**Wrong (Markdown):**
```md
## **Getting started with ROCm**
## __Installation guide__
```
**Wrong (rST):**
```rst
**Getting started with ROCm**
=============================
```
**Right:**
```md
## Getting started with ROCm
```
**Source:** ROCm best practices

---

## Writing style

### Rule: BEST-004
**Severity:** warning
**Scope:** All documentation — conciseness
**Rule:** Documentation should be written in a straightforward, concise, and clear manner. Omit needless words. Avoid filler phrases, redundant qualifiers, and overly verbose explanations.
**Wrong:**
```md
It is important to note that in order to be able to successfully install
the software, you will first need to make sure that all of the prerequisites
have been properly met.
```
**Right:**
```md
Before installing the software, verify that all prerequisites are met.
```

```routing
tier: llm
applies_when: ["*"]
strategy: whole_file
note: Conciseness / omit needless words -- quality judgment.
```

**Source:** ROCm best practices

---

### Rule: BEST-005
**Severity:** warning
**Scope:** All documentation — assumed reader proficiency
**Rule:** Assume the reader has some technical proficiency. Overview and concept documentation may assume readers understand GPU programming and the fundamentals of the ROCm stack. API documentation may assume the reader is familiar with the content of the overview and concept documentation. Do not over-explain basic concepts that the target audience is expected to know.

```routing
tier: llm
applies_when: ["*"]
strategy: whole_file
note: Assumed reader proficiency -- adequacy judgment.
```

**Source:** ROCm best practices

---

## Documentation structure

### Rule: BEST-006
**Severity:** warning
**Scope:** Library documentation — overview content
**Rule:** Overview documentation must include:
- A statement of the functionality provided by the library
- A quick tour of key concepts
- A guide on how to get started

```routing
tier: llm
applies_when: ["*"]
strategy: whole_file
note: Overview completeness (functionality/concepts/getting-started).
```

**Source:** ROCm best practices

---

### Rule: BEST-007
**Severity:** warning
**Scope:** Library documentation — concept documentation
**Rule:** Concept documentation should describe functionality, architecture, execution, or other topics in detail. Overview and concept documentation must be authored in rST.

```routing
tier: llm
applies_when: ["*"]
strategy: whole_file
note: Concept docs adequacy -- judgment.
```

**Source:** ROCm best practices

---

### Rule: BEST-008
**Severity:** warning
**Scope:** Library documentation — API reference
**Rule:** API documentation describes the usage of publicly exposed symbols (functions, classes, structs, enums). API documentation must be written in Doxygen markup in the source code. Doxygen output is consumed by Sphinx for rendering alongside rST content.
**Source:** ROCm best practices

---

## Required repository files

### Rule: BEST-009
**Severity:** error
**Scope:** Repository root — required files
**Rule:** Each repository must contain the following files in the repository root, written in Markdown:
- **README.md**: Short introduction to the library, repository contents, link to reference documentation, and a quick installation guide.
- **LICENSE.md**: License text as approved by AMD Legal.
- **CHANGELOG.md**: Changes included in each release and in development, following the standardized format for the libraries.
**Source:** ROCm best practices

---

## Embedded formats

### Rule: BEST-010
**Severity:** info
**Scope:** All documentation — LaTeX usage
**Rule:** LaTeX is used only for embedded math equations within rST and Doxygen content. Do not use LaTeX to produce whole sections or pages of documentation. For math equations, use the `.. math::` directive in rST or the corresponding MyST syntax.
**Right (rST):**
```rst
The loss function is defined as:

.. math::

   L = -\sum_{i} y_i \log(\hat{y}_i)
```
**Right (MyST Markdown):**
```md
The loss function is defined as:

$$
L = -\sum_{i} y_i \log(\hat{y}_i)
$$
```
**Source:** ROCm best practices
