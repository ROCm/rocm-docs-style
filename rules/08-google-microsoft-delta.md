# Google and Microsoft style guide deltas

This file documents only the points where ROCm custom rules explicitly
deviate from, add to, or are more lenient than the Google Developer
Documentation Style Guide or the Microsoft Writing Style Guide.

Rules where ROCm and the baselines fully agree are not listed here.
For the priority order, see `00-precedence.md`.

---

## ROCm is stricter than Google

### DELTA-001: No "we" — ever
**ROCm rule:** CORE-005
**Google says:** Use second person ("you") as the default, but allows
first-person plural ("we") when referring to the company or team
(e.g., "We recommend upgrading to the latest version").
**ROCm says:** Always use second person ("you"). Never use "we".
**Implication:** Rewrite all instances of "we" to second person or
imperative mood.
**Wrong:**
```md
We recommend installing the latest driver.
```
**Right:**
```md
Install the latest driver.
```

---

### DELTA-002: Banned heading names
**ROCm rule:** CORE-010
**Google says:** Use descriptive headings; no explicit prohibition of
specific heading names.
**Microsoft says:** Same — no banned heading names.
**ROCm says:** Do not use "Introduction", "Conclusion", "References",
"Acknowledgements", or "Appendices" as headings. Use descriptive,
content-specific headings instead.
**Implication:** Replace generic headings with content-specific ones.
**Wrong:**
```md
## Introduction
```
**Right:**
```md
## ROCm installation overview
```

---

### DELTA-003: No slashes (blanket rule)
**ROCm rule:** CORE-003
**Google says:** Avoid slashes in running text, but acknowledges
established terms where slashes are conventional (e.g., "client/server").
**ROCm says:** Use "and" or "or" instead of a slash. No exceptions for
stylistic slashes.
**Implication:** ROCm applies this more broadly than Google. Established
technical terms where the slash is part of the name remain acceptable
(e.g., "I/O", "TCP/IP") as these are proper nouns or standard
abbreviations, not stylistic slashes.

---

## ROCm is more lenient than Google

### DELTA-004: Image captions and figure labels are optional
**ROCm rule:** (rules/01-core.md, Images section)
**Google says:** Recommends including captions and figure labels for
images.
**Microsoft says:** Also recommends captions.
**ROCm says:** Naming, labeling, and captioning figures is optional.
**Implication:** Do not flag missing captions or figure labels as
violations. Alt text is still required (CORE-015).

---

## ROCm is less prescriptive than Google

### DELTA-005: Tense — "be consistent" vs. "use present tense"
**ROCm rule:** CORE-006
**Google says:** Use present tense. Avoid future tense ("will") and past
tense unless describing historical events.
**Microsoft says:** Also recommends present tense.
**ROCm says:** Use consistent tense throughout. Does not mandate present
tense specifically.
**Implication:** Present tense is preferred (per the Google baseline), but
a document written consistently in another tense is not a ROCm violation.
Flag tense inconsistency, not tense choice.

---

## ROCm adds where Google is silent

### DELTA-006: Left-align all table text
**ROCm rule:** CORE-017
**Google says:** No guidance on table text alignment.
**Microsoft says:** Left-align table text.
**ROCm says:** Left-align all table text.
**Implication:** This is a case where ROCm fills a Google gap. The rule
aligns with Microsoft's guidance.

---

### DELTA-007: Image attribution required
**ROCm rule:** CORE-016
**Google says:** No specific guidance on image attribution in
documentation.
**Microsoft says:** No specific guidance.
**ROCm says:** Provide attributions and credits for images where
applicable.
**Implication:** This is a ROCm addition.

---

### DELTA-008: "X for ROCm" product naming
**ROCm rule:** ThirdPartyProductNaming
**Google says:** N/A — product naming conventions are outside the scope
of the Google style guide.
**Microsoft says:** N/A.
**ROCm says:** When combining AMD trademarks with third-party names, use
"X for ROCm" or "X for AMD" format. Do not prefix the third-party name
with ROCm or AMD.
**Implication:** This is entirely ROCm-specific and has no baseline
equivalent.
**Wrong:**
```md
ROCm PyTorch
```
**Right:**
```md
PyTorch for ROCm
```

---

### DELTA-009: Acronym spell-out exceptions

**ROCm rule:** CORE-018
**Google says:** `Google.Acronyms` flags any 3-5 letter, all-caps token that
never appears spelled out as "Full Name (ACRONYM)" nearby, with a fixed
~60-term exceptions list (API, GPU, CPU, HTML, URL, etc.).
**Microsoft says:** N/A — Microsoft's acronym rule (`Microsoft.Acronyms`)
is not enabled in this style set.
**ROCm says:** Same detection logic as `Google.Acronyms`, but the
exceptions list is extended with AMD/ROCm proper-name acronyms that are
never spelled out in ROCm docs: AMD, SMI, LLVM, APU, SIMD, VRAM, CUDA,
HIP, CDNA, RDNA, GCN.
**Implication:** `Google.Acronyms` is disabled (`Google.Acronyms = NO`)
in `.vale.ini` and superseded by `CORE-018`. The three added terms (AMD,
CUDA, LLVM) are handled as explicit exceptions in this rule rather than
through a general accepted-terms list, because exempting them everywhere
in the documentation would prevent other, unrelated checks from correctly
flagging issues involving those same terms.
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

---

### DELTA-010: Colon capitalization known-name exceptions

**ROCm rule:** CORE-019
**Google says:** `Google.Colons` flags any capital letter immediately after
a colon followed by a space, on the theory that the word after a colon
should be lowercase unless it independently requires a capital. It has no
exceptions list.
**Microsoft says:** N/A — `Microsoft.HeadingColons` addresses a different
case (capitalization after a colon in headings) and is already disabled
in favor of the Google/CORE-008 sentence-case direction; it does not
provide a general exceptions mechanism either.
**ROCm says:** Same detection logic as `Google.Colons`, but with a
negative-lookahead exception so the check doesn't fire when the word
right after the colon is a known ROCm/AMD product, library, or
third-party proper noun (for example, "ROCm", "PyTorch", "CUDA",
"Kubernetes") rather than an ordinary word that violates sentence case.
The exception only applies to names that already start with an uppercase
letter — lowercase-leading names like hipBLAS, rocFFT, cuDNN, and vLLM
can never trigger the base `:\s[A-Z]` token in the first place.
**Implication:** `Google.Colons` is disabled (`Google.Colons = NO`) in
`.vale.ini` and superseded by `CORE-019`. "ROCm" specifically is handled
as an exception within this rule rather than through a general
accepted-terms list, for the same reason given above: a blanket exception
would prevent other checks from correctly catching genuine capitalization
errors involving that word.
**Wrong:**
```md
Note: This is important.
```
**Right:**
```md
Note: this is important.
```

**Also right (known proper noun, no lowercasing):**
```md
Requirement: ROCm 6.0 or later.
```

---

### DELTA-011: Unit-of-measure exceptions for LLM model names

**ROCm rule:** CORE-020
**Google says:** `Google.Units` flags any digit run immediately followed by
a unit token (bytes, kB/MB/GB/TB, or a time unit) with no space between
them, on the theory that it's a missing space before the unit. It has no
exceptions list.
**Microsoft says:** N/A — `Microsoft.Units` addresses the same gap and is
already disabled in favor of Google/CORE-020; it does not provide an
exceptions mechanism either.
**ROCm says:** Same detection logic as `Google.Units`, but the bare-"B"
(no metric prefix) token doesn't fire when the digit run is part of an LLM
model name's parameter-count suffix rather than a byte count — specifically
when the digits are hyphen-joined to the model name (for example,
"GPT-OSS-20B") or preceded by another bare number and a space (for example,
"Llama 3 405B", where "405B" follows the model's version number "3"). The
kB/MB/GB/TB token and the time-unit token are unchanged, since neither
collides with LLM parameter-count naming.
**Implication:** `Google.Units` is disabled (`Google.Units = NO`) in
`.vale.ini` and superseded by `CORE-020`, which encodes the LLM-model-name
exception directly in its detection pattern. Model names written as
"Name NNNB" with no hyphen and no version number in between (for example,
"Llama 70B") are not excluded and are still flagged; narrowing the
exclusion further risks swallowing genuine byte-count typos like
"Buffer 20B".
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
