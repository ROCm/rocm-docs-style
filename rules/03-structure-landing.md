# Landing page structure rules

These rules apply to component landing pages in ROCm documentation.

**Format applicability:** Examples use MyST Markdown directive syntax
(`::::{grid}`, `:::{grid-item-card}`). The equivalent rST syntax uses
`.. grid::` and `.. grid-item-card::` directives. The structural
requirements are the same regardless of format. Templates for both
formats are available in `templates/`.

## Rule: LAND-001
**Severity:** warning
**Scope:** Component landing pages — "What is" section
**Rule:** If the component description is short (two small paragraphs or fewer), place it inline on the landing page. If it is extensive, summarize it on the landing page and link to a separate "What is {componentName}?" topic.
**Wrong:**
```md
# rocExample

For a description of rocExample, see [What is rocExample?](./what-is.md)
```
(A one-sentence description should not be offloaded to a separate page.)
**Right (short):**
```md
# rocExample

rocExample provides APIs for accelerated decoding on AMD GPUs.
```
**Right (long):**
```md
# rocExample

rocExample provides APIs for accelerated decoding on AMD GPUs. To learn
more, see [What is rocExample?](./what-is-rocexample.md).
```

```routing
tier: llm
applies_when: [is_landing_page]
strategy: whole_file
note: Landing-page description length/quality -- semantic judgment.
```

**Source:** ROCm custom

---

## Rule: LAND-002
**Severity:** error
**Scope:** Component landing pages — GitHub link
**Rule:** The link to the component's GitHub repository must appear immediately after the component description, before the topic table.
**Wrong:**
```md
# rocExample

rocExample provides APIs for accelerated decoding.

::::{grid}
(topic cards)
::::

The rocExample public repository is located at ROCm/rocExample.
```
**Right:**
```md
# rocExample

rocExample provides APIs for accelerated decoding.

The rocExample public repository is located at
[ROCm/rocExample](https://github.com/ROCm/rocExample).

::::{grid}
(topic cards)
::::
```
**Source:** ROCm custom

---

## Rule: LAND-003
**Severity:** error
**Scope:** Component landing pages — topic organization
**Rule:** The topic table must follow this fixed order. Omit sections that do not apply, but never reorder them.
1. Install
2. Conceptual
3. How to
4. Samples, examples, or tutorials
5. Reference
**Wrong:** Placing "Reference" before "How to."
**Right:** Following the order listed above; omitting "Samples" if none exist.
**Source:** ROCm custom (inspired by Diataxis)

---

## Rule: LAND-004
**Severity:** error
**Scope:** Component landing pages — structural boilerplate
**Rule:** Do not include the line "The documentation is structured as follows" or similar structural preambles between the Install section and the rest of the landing page.
**Wrong:**
```md
The documentation is structured as follows:
```
**Right:** Remove the line entirely. The topic table is self-explanatory.
**Source:** ROCm custom

---

## Rule: LAND-005
**Severity:** error
**Scope:** Component landing pages — installation vs. building
**Rule:** Instructions for building from source must be separated from package installation instructions. They must not be combined on a single page or under a single heading.
**Wrong:**
```md
:::{grid-item-card} Install
* [Installing rocExample](./install.md)
:::
```
(where `install.md` mixes package install and build-from-source)
**Right:**
```md
:::{grid-item-card} Install
* [Installing rocExample with the package installer](./install/package-install.md)
* [Building rocExample from source code](./install/build-from-source.md)
:::
```

```routing
tier: llm
applies_when: [is_landing_page]
strategy: whole_file
note: Build-vs-install mixed on one page -- needs reading page.
```

**Source:** ROCm custom

---

## Rule: LAND-006
**Severity:** error
**Scope:** Component landing pages — "Quick Start" heading
**Rule:** Do not use "Quick Start" for package installation instructions. Use "package installation" or "Installing {componentName} with the package installer" instead.
**Wrong:**
```md
* [Quick Start](./quick-start.md)
```
**Right:**
```md
* [Installing rocExample with the package installer](./install/package-install.md)
```
**Source:** ROCm custom

---

## Rule: LAND-007
**Severity:** warning
**Scope:** Component landing pages — installation prerequisites
**Rule:** Installation prerequisites must be listed as a separate entry in the Install section, not buried within the installation instructions.
**Wrong:**
```md
:::{grid-item-card} Install
* [Installing rocExample](./install.md)
:::
```
(where prerequisites are a subsection inside `install.md`)
**Right:**
```md
:::{grid-item-card} Install
* [rocExample installation prerequisites](./install/prerequisites.md)
* [Installing rocExample with the package installer](./install/package-install.md)
:::
```

```routing
tier: llm
applies_when: [is_landing_page]
strategy: structural
section_scope: true
note: Prerequisites buried in instructions -- structure + meaning.
```

**Source:** ROCm custom

---

## Rule: LAND-008
**Severity:** error
**Scope:** Component landing pages — contributing section placement
**Rule:** The contributing section must appear last on the landing page, after all topic cards.
**Wrong:** Placing the contributing link inside the topic table or before the Reference card.
**Right:** A standalone line or card at the bottom of the page.
**Source:** ROCm custom

---

## Rule: LAND-009
**Severity:** warning
**Scope:** Component landing pages — contributing section format
**Rule:** If there is only one contributing page, use a single line (not a card). If there are multiple contributing pages, use a separate card.
**Wrong (single page in a card):**
```md
:::{grid-item-card} Contributing
* [Contributing to rocExample](./contributing.md)
:::
```
**Right (single page):**
```md
For information on contributing to the rocExample code base, see
[Contributing to rocExample](./contributing.md).
```
**Right (multiple pages):**
```md
:::{grid-item-card} Contributing
* [Contributing to rocExample](./contributing/index.md)
* [Code of Conduct](./contributing/code-of-conduct.md)
:::
```
**Source:** ROCm custom
