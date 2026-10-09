# Suspended checks and checks left to the review tier

Vale is the mechanical half of the ROCm style check. Some checks were switched
off after they were run over real ROCm documentation, because they produced
mostly false positives or contradicted ROCm policy. This page records each one,
why it is off, and who is expected to cover the gap, so that a check is never
dropped silently and nobody has to rediscover why.

Each check is disabled by a single line in `vale/.vale.ini`, next to a comment
giving the reason. To bring one back, delete that line. Checks that were
replaced by a ROCm rule, or switched off only because another check already
covers the same thing, are listed in the table in the repository README and are
not repeated here.

## Left to the LLM review tier

These need the sentence read to judge. Vale does not check them. Whether the
LLM tier covers a given item is that tier's decision; this list is what it
should be handed.

| Check | What it flagged | Why it cannot be mechanical |
|---|---|---|
| `Google.Will` | The word "will" | A genuine future event ("will be fixed in a future release") cannot be told from a present-tense candidate ("CRIU will fail") without reading the sentence. |
| `Microsoft.Adverbs` (replaced by `CORE-026`) | 264 adverbs | Most carry technical meaning: "silently" (a failure that reports no error), "randomly" (stochastic sampling), "gracefully" (degradation behavior). Only pure intensifiers are checked mechanically now. |
| `Microsoft.UIVerbs` | "click", and similar input-specific verbs | "Click" is correct for a literal mouse action and wrong for a generic one. |
| Sentence case for headings that begin with a lowercase letter (reStructuredText) | A heading such as `dynamic_dimension` | These are API identifiers and are exempt from the mechanical check, so a heading that merely forgets to capitalize its first word is not caught. |
| Proper nouns in headings that are not on the shared list | A product name written in Title Case | The mechanical check only knows the names in `wordlists/heading-proper-nouns.txt`. |

## Suspended, not covered by anything

These are off and nothing replaces them.

| Check | What it flagged | Why it is off |
|---|---|---|
| `ROCm.CORE-022` | A `v` before a version number | Standard names such as "Inception v3" and "PKCS#1 v1.5" use the prefix, as do some AMD releases. The rule file is kept so it can be re-enabled. |
| `Microsoft.Foreign` | "e.g." and "i.e." (also "viz." and "ergo") | "e.g." and "i.e." are allowed in this docs set. Dropping the check also drops "viz." and "ergo", which are rare. |
| `Microsoft.Quotes` | Punctuation outside quotation marks | Technical documentation quotes exactly what is typed. |
| `Microsoft.GeneralURL` | "URL" | The audience is technical, so "URL" is correct. |
| `Microsoft.Terms` | "numerical" | "Numeric" and "numerical" are not interchangeable ("numerical methods"). |
| `Microsoft.Suspended` | "pre- and post-" | No ROCm rule asks for this. |
| `Google.LyHyphens` | Any word ending in "-ly" followed by a hyphen | It matches words that are not adverbs ("multiply-add", "only-if-needed"). |
| `Vale.Repetition` | A repeated word | Almost every hit was a repeated name ("Si Si") or version number ("7.x.x"). It is built in and cannot be tuned. A real typo such as "the the" is no longer caught mechanically. |
| `ROCm.SPELL-009` entries: "simple", "simply", "easy", "easily", "please" | Subjective or filler words | Ordinary technical English that writers use deliberately. See the note under `SPELL-009` in `02-spelling-terminology.md`. |
| `ROCm.CORE-024` entries: "above", "open-source", "functionality", "abort", "SHA1" | Word-choice swaps inherited from Google | "above" is used as a Right example in `03-structure-landing.md`; `SPELL-006` defers "open-source" to human judgment; the other three change meaning or suggest nonsense. See `CORE-024` in `01-core.md`. |

## Known limitations of checks that are on

These are not suspended, but a writer should know about them.

| Check | Limitation |
|---|---|
| `ROCm.CORE-008-MD` | A `#` comment line inside a fenced code block is read as a heading. A fence-aware version was tried and rejected: it was about 25 times slower on a 300 KB file and returned wrong results at that size. |
| `ROCm.CORE-008` (reStructuredText) | A phrase that starts with a word containing two or more capitals (`ROCr Runtime`, `MI300 Series`) cannot be exempted, so those names are tagged Markdown-only in the shared list. |
| `ROCm.CORE-003` | A relative path with no leading slash and no extension (`rocm/jax-community`, `usr/bin/env`) looks the same as "read/write" and is flagged. Put it in a code span, or suppress it inline as the README describes. |
| `ROCm.CORE-020` | "0s" and "1s" meaning zeros and ones look like seconds and are flagged. |
