# Metadata and SEO rules

These rules apply to metadata, page titles, URLs, images, and SEO practices
in ROCm documentation.

## Meta tags

### Rule: META-001
**Severity:** error
**Scope:** All documentation pages — meta description
**Rule:** Every page must include a `meta description` tag. In reStructuredText, use `.. meta:: :description:` — this directive must be the first element in the file, above the page title. In MyST Markdown, use YAML front matter under `myst: html_meta: "description"`.
**Wrong (rst):**
```rst
****************************
ROCm documentation structure
****************************
```
(No meta description.)
**Right (rst):**
```rst
.. meta::
   :description: Learn about how ROCm libraries and tools structure their documentation.

****************************
ROCm documentation structure
****************************
```
**Right (MyST Markdown):**
```markdown
---
myst:
    html_meta:
        "description": "Learn about how ROCm libraries and tools structure their documentation."
---
# ROCm documentation structure
```
**Source:** ROCm custom

---

### Rule: META-002
**Severity:** warning
**Scope:** All documentation pages — meta description length
**Rule:** Meta descriptions should be 150-160 characters. Longer descriptions are truncated in search results.
**Wrong:**
```
"description": "This page is about ROCm."
```
(Too short to be useful.)
**Wrong:**
```
"description": "This page provides a comprehensive overview of all the different
ways you can install, configure, optimize, and deploy ROCm on your system including
all supported Linux distributions and Windows environments with detailed step-by-step
instructions for each platform."
```
(Will be truncated.)
**Right:**
```
"description": "Learn how to install and configure ROCm on supported Linux distributions and Windows. Includes prerequisites, package install, and build-from-source."
```
**Source:** ROCm custom, Google Search Central

---

### Rule: META-003
**Severity:** warning
**Scope:** All documentation pages — meta description style
**Rule:** Meta descriptions should use action-oriented language (e.g., "Learn more about...", "Discover how to...") and accurately reflect the page content.
**Wrong:**
```
"description": "ROCm installation"
```
**Right:**
```
"description": "Learn how to install ROCm using the package manager or build it from source on supported Linux distributions."
```

```routing
tier: llm
applies_when: [has_frontmatter]
strategy: whole_file
note: Meta-description action-oriented + accurate -- quality judgment.
```

**Source:** ROCm custom

---

### Rule: META-004
**Severity:** warning
**Scope:** All documentation pages — meta keywords
**Rule:** Every page should include a `meta keywords` tag with relevant terms, including terms users might search for that are not explicitly in the page content. Include competitor or migration-related terms (e.g., CUDA) where appropriate for discoverability.
**Wrong:**
```
"keywords": "ROCm"
```
(Too few keywords.)
**Right:**
```
"keywords": "ROCm, GPU, installation, Linux, HIP, CUDA migration, AMD Instinct, accelerator"
```

```routing
tier: hybrid
applies_when: [has_frontmatter]
strategy: whole_file
note: Keyword presence is Script; relevance/quality is LLM.
```

**Source:** ROCm custom

---

## Titles and headings

### Rule: META-005
**Severity:** error
**Scope:** All documentation pages — page title (h1)
**Rule:** The page title (h1) must be descriptive, concise (50-60 characters), and include primary keywords. It must accurately reflect the page content. Avoid generic titles.
**Wrong:**
```md
# System requirements
```
(Ambiguous — which product's system requirements?)
**Right:**
```md
# HIP SDK system requirements
```

```routing
tier: hybrid
applies_when: [has_frontmatter]
strategy: whole_file
note: Title length is Script; reflects-content judgment is LLM.
```

**Source:** ROCm custom

---

### Rule: META-006
**Severity:** warning
**Scope:** All documentation pages — TOC vs. page title consistency
**Rule:** The page title and its table of contents (TOC) anchor text should be consistent. If a shorter TOC entry is used for brevity, the broader context (section headings, TOC hierarchy) must make the subject clear.

```routing
tier: llm
applies_when: [has_frontmatter]
strategy: whole_file
note: Title/TOC consistency in context -- semantic.
```

**Source:** ROCm custom

---

## Images

### Rule: META-007
**Severity:** warning
**Scope:** All documentation pages — image file names
**Rule:** Image file names must be descriptive and keyword-rich, using dash-case. Do not use generic names like `IMG_1234.jpg` or `screenshot.png`.
**Wrong:** `IMG_1234.jpg`, `figure1.png`
**Right:** `gpu-inference-optimization.jpg`, `rocm-install-workflow.png`
**Source:** ROCm custom, Google Search Central

---

### Rule: META-008
**Severity:** error
**Scope:** All documentation pages — image alt text
**Rule:** All images must have descriptive alt text that conveys the image's purpose. Do not keyword-stuff alt text. Use `alt=""` only for purely decorative images.
**Wrong:** `gpu`, `gpu performance`, `inference gpu`
**Right:** `GPU used for deep learning inference optimization`

```routing
tier: hybrid
applies_when: [has_image]
strategy: structural
section_scope: true
note: Alt-text presence is Script; descriptive-vs-keyword-stuffed is LLM.
```

**Source:** ROCm custom, Google Search Central

---

### Rule: META-009
**Severity:** warning
**Scope:** All documentation pages — image format
**Rule:** Use the appropriate image format: JPEG for photos, PNG for images requiring transparency or higher quality, WebP for modern browsers when better compression is needed.
**Source:** ROCm custom

---

## URLs and file names

### Rule: META-010
**Severity:** error
**Scope:** All files — URL-friendly file names
**Rule:** File names must be descriptive and use hyphens (dashes) to separate words. Do not use underscores (search engines do not index them properly), spaces, or generic names.
**Wrong:** `chapter1.md`, `my_new_file.rst`, `page123.md`
**Right:** `seo-tactics-guide.md`, `hip-sdk-installation.rst`
**Source:** ROCm custom

---

### Rule: META-011
**Severity:** error
**Scope:** All pages — URL stability
**Rule:** Avoid changing URLs after publication. If a URL change is necessary, implement a 301 redirect from the old URL to the new one. Do not create redirect chains (A -> B -> C).

```routing
tier: llm
applies_when: ["*"]
strategy: whole_file
note: URL stability needs site/history context -- not single-file.
```

**Source:** ROCm custom

---

### Rule: META-012
**Severity:** warning
**Scope:** All pages — orphan pages
**Rule:** Every page must be linked from at least one other page, typically via the TOC. Orphan pages (pages not linked from anywhere) hurt crawlability and discoverability.
**Source:** ROCm custom

---

## Content quality

### Rule: META-013
**Severity:** error
**Scope:** All pages — duplicate content
**Rule:** Do not create multiple pages with substantially similar content. Consolidate into a single comprehensive page. If duplication is unavoidable, use canonical tags to indicate the preferred version.

```routing
tier: llm
applies_when: ["*"]
strategy: whole_file
note: Duplicate/near-duplicate content -- semantic similarity.
```

**Source:** ROCm custom

---

### Rule: META-014
**Severity:** warning
**Scope:** All pages — keyword cannibalization
**Rule:** Do not create multiple pages targeting the same primary keyword. Each page should have a distinct primary keyword or topic.

```routing
tier: llm
applies_when: ["*"]
strategy: whole_file
note: Keyword cannibalization -- semantic overlap across pages.
```

**Source:** ROCm custom

---

### Rule: META-015
**Severity:** error
**Scope:** All pages — low-content pages
**Rule:** Avoid publishing pages with very little original content. Every page must provide substantive value.

```routing
tier: llm
applies_when: ["*"]
strategy: whole_file
note: Thin/low-content pages -- substantive-value judgment.
```

**Source:** ROCm custom

---

### Rule: META-016
**Severity:** warning
**Scope:** All pages — link anchor text
**Rule:** Anchor text in links must clearly describe where the link points. Do not use generic anchors like "here" or "click this". Use keyword-rich, descriptive text.
**Wrong:**
```md
For more information, click [here](./install.md).
```
**Right:**
```md
For more information, see [ROCm installation instructions](./install.md).
```
**Source:** ROCm custom, Google Developer Documentation Style Guide

---

## PR review checklist

### Rule: META-017
**Severity:** warning
**Scope:** Pull request reviews
**Rule:** When reviewing documentation PRs, reviewers must check the following metadata items: meta description, meta keywords, and page title (h1).
**Source:** ROCm custom
