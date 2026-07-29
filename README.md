# rocm-docs-style

A [Vale](https://vale.sh) style guide for ROCm documentation. It provides a set
of rules, wordlists, and CI tooling for catching style, spelling, and
terminology issues in ROCm docs before they're merged.

The rule set is layered on top of two established baselines:

1. **ROCm custom rules** — product-specific conventions (heading case,
   trademarks, environment-variable formatting, ROCm/AMD product-name casing,
   and more).
2. **[Google Developer Documentation Style Guide](https://developers.google.com/style)**
   and **[Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/)**
   — used as general-purpose baselines, with a handful of checks disabled
   where a ROCm rule supersedes them (see [Configuration](#configuration)
   below).

## Local usage

### 1. Install Vale

Download a Vale release from [vale-cli/vale](https://github.com/vale-cli/vale)
(the workflows in this repo install the latest release — see
[.github/workflows/self-check.yml](.github/workflows/self-check.yml) — and any
recent Vale release works locally). See the
[Vale installation docs](https://vale.sh/docs/vale-cli/installation/) for
platform-specific instructions (Homebrew, Scoop, binary download, etc.).

Verify it's on your `PATH`:

```sh
vale --version
```

### 2. Sync the Google and Microsoft style packages

This repo's config references the Google and Microsoft Vale packages, but
they aren't checked into this repository — only the ROCm-specific rules in
[vale/styles/ROCm/](vale/styles/ROCm/) are committed. Run `vale sync` from
the `vale/` directory (where [`.vale.ini`](vale/.vale.ini) lives) to download
them:

```sh
cd vale
vale sync
```

This creates `vale/styles/Google/` and `vale/styles/Microsoft/` locally. You
only need to re-run this when the packages update or after a fresh clone.

### 3. Run Vale

Point Vale at this repo's config with `--config`, then pass it a file or
directory to lint. From the root of this repository:

```sh
# Lint a single file
vale --config=vale/.vale.ini path/to/doc.md

# Lint a whole docs directory
vale --config=vale/.vale.ini path/to/docs/

# Lint everything from a consuming repo, run from that repo's root
vale --config=/path/to/rocm-docs-style/vale/.vale.ini .
```

### Reading the output

Vale reports one finding per line, in the form:

```
 <line>:<column>  <severity>  <message>  <rule ID>
```

For example:

```
 12:3  error  CORE-008: Use sentence case for headings (capitalize only the first word and proper nouns).  ROCm.CORE-008
```

- **Severity** is one of `suggestion`, `warning`, or `error`. Vale exits
  with an error only when an `error` is present.
- **Rule ID** (e.g. `ROCm.CORE-008`, `Google.Passive`, `Microsoft.Contractions`)
  identifies which style and rule fired. ROCm-specific rules are documented in
  human-readable form under [rules/](rules/) — the rule ID's suffix (e.g.
  `CORE-008`) corresponds to a section in those files.

## CI usage

To lint documentation PRs in another repository, copy
[gh-workflows/consumer-example.yml](gh-workflows/consumer-example.yml) into
that repository's `.github/workflows/` directory.

The workflow:

1. Checks out the consuming repo's PR content.
2. Checks out this repository (the style rules).
3. Downloads the latest Vale release.
4. Runs `vale sync` to fetch the Google and Microsoft packages.
5. Runs Vale, scoped to only the `.md` and `.rst` files the PR changed
   (diffed against the PR's base commit) — it does not lint the whole repo on
   every PR.

It runs entirely on GitHub-hosted runners and requires no secrets or external
services. Adjust the checkout path in the workflow if your repository layout
differs from the template's assumptions.

## Configuration

The Vale configuration lives at [`vale/.vale.ini`](vale/.vale.ini), not at
the repository root. Key points:

- `StylesPath = styles` — style packages live in [vale/styles/](vale/styles/),
  resolved relative to the `.vale.ini` file.
- `MinAlertLevel = suggestion` — all findings are reported, including
  low-severity suggestions.
- `BasedOnStyles = Vale, Google, Microsoft, ROCm` — applied to all `.md`
  files.

A few upstream Google/Microsoft checks are turned off because a ROCm rule
supersedes them:

| Disabled check | Why |
|---|---|
| `Vale.Spelling` | ROCm/AMD product and library names (e.g. ROCm, hipBLAS, MIOpen) aren't in standard dictionaries, and this repo doesn't ship a custom spelling vocabulary. Casing and spelling of these names is enforced by the `ROCm.SPELL-*` rules instead. |
| `Google.Headings`, `Microsoft.Headings` | `ROCm.CORE-008` owns sentence-case heading capitalization, with its own exceptions list for product and library names. |
| `Google.Acronyms`, `Google.Colons`, `Google.Units` | `ROCm.CORE-018`/`CORE-019`/`CORE-020` supersede these with ROCm/AMD-aware detection logic (extended acronym exceptions, proper-noun-aware colon casing, and unit-of-measure handling). |

## Structure

| Path | Contents |
|---|---|
| [vale/.vale.ini](vale/.vale.ini) | Vale configuration |
| [vale/styles/ROCm/](vale/styles/ROCm/) | ROCm-specific Vale rules (committed) |
| [vale/styles/Google/](vale/styles/Google/), `vale/styles/Microsoft/` | Google/Microsoft Vale packages (fetched via `vale sync`, not committed) |
| [wordlists/](wordlists/) | Term lists: AMD trademarks, third-party trademarks, banned/restricted terms, and preferred terminology |
| [rules/](rules/) | Human-readable documentation of the ROCm rule set, organized by topic |
| [gh-workflows/consumer-example.yml](gh-workflows/consumer-example.yml) | Template CI workflow for consuming repos |

## Contributing

Rule definitions live in [vale/styles/ROCm/](vale/styles/ROCm/) as Vale YAML
rules; their rationale and examples are documented in [rules/](rules/).
Terminology and trademark lists live in [wordlists/](wordlists/).

To propose a rule change, open a pull request. [self-check.yml](.github/workflows/self-check.yml)
validates that the Vale config still loads and lints any Markdown your PR
changes against the repo's own rules.
