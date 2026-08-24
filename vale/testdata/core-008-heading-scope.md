<!--
Regression fixture for CORE-008/CORE-008-MD: constrain heading-case detection
to actual headings (ATX `#` in Markdown), not anything that merely looks like
one. Run: `vale --config=vale/.vale.ini vale/testdata/core-008-heading-scope.md`

Expected: zero CORE-008/CORE-008-MD findings. Before the fix, Vale (via
goldmark) treated a paragraph immediately followed by a bare `---`/`===`
divider (no blank line) as a CommonMark Setext heading, so a non-heading line
containing a colon or title-case words could get flagged as if it were a
malformed heading.
-->

# Getting started with ROCm

This line contains a Colon: And Title Case Words, immediately followed by a
divider with no blank line in between -- this must NOT be treated as a
heading.
---

More prose right after the divider.

## AMD EPYC processors overview

This line ends with a colon: it is ordinary prose, not a heading.
