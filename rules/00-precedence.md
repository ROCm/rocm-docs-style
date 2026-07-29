# Rule precedence

## Priority order

When rules conflict, apply them in this order (highest priority first):

1. **ROCm custom rules** (`01-core.md`, `03-structure-landing.md`,
   `04-metadata.md`, `05-env-variables.md`)
2. **Google Developer Documentation Style Guide**
   https://developers.google.com/style
3. **Microsoft Writing Style Guide** (only when Google does not provide
   explicit guidance)
   https://learn.microsoft.com/en-us/style-guide/welcome/

A ROCm custom rule always wins. Google is the primary baseline. Microsoft
is the fallback when Google is silent on a topic.

## Baseline coverage

The Google and Microsoft guides are **not** reproduced in this rule set.
Claude has built-in knowledge of both. The file `08-google-microsoft-delta.md`
documents only the points where ROCm explicitly deviates from or emphasizes
specific rules in those guides.

When reviewing documentation, apply the full Google guide as the default,
except where a ROCm rule explicitly overrides it. If a topic is not covered
by either Google or ROCm rules, consult the Microsoft guide.

## Cross-reference index

Several rules cover the same topic from different angles (style vs. SEO).
When both trigger on the same content, report the higher-severity rule and
note the related rule. Do not report the same violation twice.

| Topic | Primary rule | Related rule(s) | Notes |
|---|---|---|---|
| File naming | CORE-007 (style) | META-010 (SEO) | Same requirement; report once |
| Link anchor text | CORE-012 (style) | META-016 (SEO) | Same requirement; report once |
| Image alt text | CORE-015 (style) | META-008 (SEO) | CORE-015 adds "don't start with 'this is an image of'"; META-008 adds keyword guidance |
| Headings: no stacking | CORE-009 (style) | META-005 (SEO) | Both reinforce the same practice |
| Orphan pages | META-012 (SEO) | — | No style equivalent; SEO-only concern |
| Duplicate content | META-013 (SEO) | — | No style equivalent; SEO-only concern |

## Spelling authority

American English as defined by the Merriam-Webster dictionary is the
authoritative spelling reference. See `02-spelling-terminology.md` for
ROCm-specific terminology choices. When Merriam-Webster lists multiple
acceptable spellings, prefer the first (primary) entry.
