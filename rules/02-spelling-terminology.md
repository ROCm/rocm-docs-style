# Spelling and terminology rules

These rules govern spelling, terminology, and word choice in ROCm
documentation.

## Spelling

### Rule: SPELL-001
**Severity:** error
**Scope:** All documentation — American English
**Rule:** Use American English spelling as defined by the Merriam-Webster dictionary. When Merriam-Webster lists multiple acceptable spellings, use the first (primary) entry.
**Wrong:** `colour`, `behaviour`, `licence` (noun), `analyse`, `catalogue`, `centre`, `grey`, `judgement`, `modelling`
**Right:** `color`, `behavior`, `license`, `analyze`, `catalog`, `center`, `gray`, `judgment`, `modeling`
**Source:** ROCm custom

---

### Rule: SPELL-002
**Severity:** warning
**Scope:** All documentation — common American vs. British variants
**Rule:** Prefer the following American English spellings. This list captures the most frequently encountered variants in technical documentation.

| Use (American) | Not (British) |
|---|---|
| analog | analogue |
| analyze | analyse |
| artifact | artefact |
| canceled | cancelled |
| canceling | cancelling |
| catalog | catalogue |
| center | centre |
| color | colour |
| customize | customise |
| defense | defence |
| dialog | dialogue (for UI); dialogue (for conversation) is acceptable |
| favor | favour |
| fiber | fibre |
| fulfill | fulfil |
| gray | grey |
| honor | honour |
| initialize | initialise |
| judgment | judgement |
| labeled | labelled |
| license | licence (noun) |
| modeling | modelling |
| optimize | optimise |
| organization | organisation |
| parallelize | parallelise |
| program | programme (except in proper nouns) |
| realize | realise |
| recognize | recognise |
| serialize | serialise |
| signaling | signalling |
| synchronize | synchronise |
| utilize | utilise |
| virtualize | virtualise |

**Source:** ROCm custom, Merriam-Webster

---

## Terminology

### Rule: SPELL-003
**Severity:** error
**Scope:** All documentation — ROCm product and library names
**Rule:** ROCm library and tool names have specific capitalization that must be preserved exactly. These are not regular words and must not be spell-checked or autocorrected.

Key examples:

| Correct | Wrong |
|---|---|
| ROCm | ROCM, rocm, Rocm |
| hipBLAS | HipBLAS, HIPBLAS, hipblas |
| rocBLAS | RocBLAS, ROCBLAS, rocblas |
| MIOpen | miopen, MIOPEN, Miopen |
| rocFFT | RocFFT, ROCFFT, rocfft |
| hipSPARSE | HipSPARSE, hipsparse |
| rocSOLVER | RocSOLVER, rocsolver |
| MIGraphX | migraphx, MIGRAPHX |
| ROCProfiler | rocprofiler, ROCPROFILER |
| rocPRIM | RocPRIM, rocprim |
| rocRAND | RocRAND, rocrand |
| rocThrust | RocThrust, rocthrust |
| rocALUTION | rocalution, ROCALUTION |
| AMD EPYC | Epyc, epyc |
| AMD Instinct | instinct, INSTINCT |
| RDNA | rdna, Rdna |
| CDNA | cdna, Cdna |
| vLLM | VLLM, Vllm |
| ASan | ASAN |
| rocpd | ROCPD |

**Note:** `rocprofiler-compute` and `rocprofiler-systems` are the package names for
ROCm Compute Profiler and ROCm Systems Profiler, respectively. These are distinct
tools from ROCProfiler (the profiling library) and are acceptable as-is — do not
"correct" them to `ROCProfiler-compute`/`ROCProfiler-systems`.
**Source:** ROCm custom, Vale vocabulary

---

### Rule: SPELL-004
**Severity:** warning
**Scope:** All documentation — compound words
**Rule:** Use the following compound word forms consistently. These are drawn from established ROCm documentation conventions.

| Correct | Wrong |
|---|---|
| backend | back-end, back end |
| changelog | change log, change-log |
| checkpoint | check-point, check point |
| codename | code-name, code name |
| command line (noun) | commandline |
| command-line (adjective) | commandline, command line (adj.) |
| dataset | data-set, data set |
| datatype | data-type, data type |
| filename | file-name, file name |
| filesystem | file-system, file system |
| hostname | host-name, host name |
| namespace | name-space, name space |
| runtime | run-time, run time |
| toolchain | tool-chain, tool chain |
| walkthrough | walk-through, walk through |
| whitepaper | white-paper, white paper |
| whitespace | white-space, white space |
| workflow | work-flow, work flow |
| workgroup | work-group, work group |
| workload | work-load, work load |

**Source:** ROCm custom, Vale vocabulary

---

### Rule: SPELL-005
**Severity:** warning
**Scope:** All documentation — abbreviation and acronym casing
**Rule:** Technical abbreviations and acronyms must use their established casing. Do not normalize to all-uppercase or all-lowercase unless that is the established form.

| Correct | Wrong |
|---|---|
| GPU, GPUs | Gpu, gpu |
| CPU, CPUs | Cpu, cpu |
| API, APIs | Api, api |
| PCIe | PCIE, pcie |
| OpenCL | Opencl, OPENCL |
| OpenMP | Openmp, OPENMP |
| CUDA | Cuda, cuda |
| LLVM | Llvm, llvm |
| CMake | CMAKE, cmake (in prose) |
| NumPy | Numpy, NUMPY |
| PyTorch | Pytorch, pytorch (in prose) |
| TensorFlow | Tensorflow, tensorflow |
| DMA | dma |
| RDMA | rdma |
| NUMA | numa |
| BLAS | blas |
| FFT | fft |
| HPC | hpc |
| MPI | mpi |

**Note:** In code blocks, file paths, and CLI commands, the casing used by the tool itself takes precedence (e.g., `cmake` as a command is correct).
**Source:** ROCm custom, Vale vocabulary

---

### Rule: SPELL-006
**Severity:** warning
**Scope:** All documentation — preferred technical terms
**Rule:** Use the following preferred forms for common technical concepts.

| Preferred | Avoid |
|---|---|
| allowlist | whitelist |
| denylist | blacklist |
| primary | master (in non-git contexts) |
| replica | slave |
| confidence check | sanity check |
| workaround | work-around |
| open source (noun) | open-source (noun) |
| open-source (adjective) | open source (adj.) |
| machine learning | Machine Learning, Machine learning |
| ML | ml |

**Source:** ROCm custom, inclusive language guidelines

---

## Word choice

### Rule: SPELL-007
**Severity:** warning
**Scope:** All documentation — Google word list
**Rule:** Consult the [Google Developer Documentation Style Guide word list](https://developers.google.com/style/word-list) for guidance on word choice. The word list covers not only words with negative connotations but also words that are ambiguous, don't translate well, or aren't descriptive. Follow the word list's recommendations for preferred alternatives.

```routing
tier: llm
applies_when: ["*"]
strategy: whole_file
note: Open-ended word-choice judgment beyond Vale substitution lists.
```

**Source:** ROCm custom, Google Developer Documentation Style Guide

---

### Rule: SPELL-008
**Severity:** warning
**Scope:** All documentation — "may" vs. "might" vs. "can"
**Rule:** Do not use "may" in technical documentation. Use "might" when expressing possibility and "can" when expressing ability or permission.
**Wrong:**
```md
You may encounter an error if the driver is outdated.
You may use the `--verbose` flag for more output.
```
**Right:**
```md
You might encounter an error if the driver is outdated.
You can use the `--verbose` flag for more output.
```
**Source:** ROCm custom, Google word list

---

### Rule: SPELL-009
**Severity:** warning
**Scope:** All documentation — ambiguous and non-translatable words
**Rule:** Avoid words that are ambiguous, don't translate well, or aren't descriptive. The following are common examples from the Google word list. This is not exhaustive — consult the full word list when uncertain.

| Avoid | Preferred | Reason |
|---|---|---|
| comprise | consist of, contain, include | Frequently misused; doesn't translate well |
| desire | want, need | Overly formal |
| e.g. | for example, such as | Doesn't translate; some readers don't know what it means |
| i.e. | that is, in other words | Same as above |
| leverage (verb) | use, take advantage of | Jargon; imprecise |
| modify | change, update, edit | "Modify" can be ambiguous in some contexts |
| please | (omit) | Unnecessary in technical writing |
| simple, simply | (omit or rephrase) | Subjective; what's simple for one reader isn't for another |
| easy, easily | (omit or rephrase) | Same as above |
| obviously | (omit) | Condescending; if it were obvious, you wouldn't need to say it |
| just | (omit or rephrase) | Minimizing; often filler |
| in order to | to | Unnecessarily wordy |
| utilize | use | Unnecessarily complex |
| via | through, using, by | Doesn't translate well |

**Source:** ROCm custom, Google word list
