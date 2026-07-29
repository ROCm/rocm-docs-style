# Environment variable documentation rules

These rules apply to pages that document environment variables in ROCm documentation.

**Format applicability:** Examples use Markdown pipe-table syntax. In rST,
use `.. list-table::` or grid tables with the same column structure. The
content requirements (columns, value formatting, descriptions) are the
same regardless of format. Templates for both formats are available in
`templates/`.

## Rule: ENV-001
**Severity:** error
**Scope:** Environment variable pages — structure
**Rule:** All environment variables for a component must be documented on a single page. Do not scatter them across multiple pages.
**Wrong:** Documenting `MY_VAR` in `install.md` and `YOUR_VAR` in `usage.md`.
**Right:** A single dedicated page (e.g., `environment-variables.md`) listing all variables.

```routing
tier: llm
applies_when: [env_var_shape]
strategy: whole_file
note: Env vars on a single page -- needs cross-page grouping context.
```

**Source:** ROCm custom

---

## Rule: ENV-002
**Severity:** error
**Scope:** Environment variable pages — grouping
**Rule:** Environment variables must be sorted by type or category. Variables of the same type must be grouped under the same heading.
**Wrong:**
```md
## Environment variables

Environment variable | Default value | Values
---------------------|---------------|-------
`COMPILER_FLAG` | ... | ...
`LOG_LEVEL` | ... | ...
`COMPILER_OPT` | ... | ...
```
(Compiler and logging variables mixed in one table with no grouping.)
**Right:**
```md
## Compiler variables

Environment variable | Default value | Values
---------------------|---------------|-------
`COMPILER_FLAG` | ... | ...
`COMPILER_OPT` | ... | ...

## Logging variables

Environment variable | Default value | Values
---------------------|---------------|-------
`LOG_LEVEL` | ... | ...
```

```routing
tier: llm
applies_when: [env_var_shape]
strategy: structural
section_scope: true
note: Variables grouped/sorted by type/category -- semantic categorization.
```

**Source:** ROCm custom

---

## Rule: ENV-003
**Severity:** warning
**Scope:** Environment variable pages — category description
**Rule:** Each type or category heading must be followed by a short blurb explaining what the environment variables in that section are used for, before the table.
**Wrong:**
```md
## Compiler variables

Environment variable | Default value | Values
---------------------|---------------|-------
```
(No explanatory text between heading and table.)
**Right:**
```md
## Compiler variables

These variables control which compiler backend is used during the build process.

Environment variable | Default value | Values
---------------------|---------------|-------
```
**Source:** ROCm custom

---

## Rule: ENV-004
**Severity:** error
**Scope:** Environment variable tables — column structure
**Rule:** Environment variable tables must use this column layout: `Environment variable | Default value | Values`. The variable name must be in backtick-delimited code font, followed by a `<br>` and a description on the same cell.
**Wrong:**
```md
Name | Description | Default | Values
-----|-------------|---------|-------
MY_ENV_VAR | Does things | 1 | 0, 1, 2
```
**Right:**
```md
Environment variable | Default value | Values
---------------------|---------------|-------
`MY_ENV_VAR` <br> Does things. | `1` | `0`: Does nothing <br> `1`: Does something
```
**Source:** ROCm custom

---

## Rule: ENV-005
**Severity:** error
**Scope:** Environment variable tables — values format
**Rule:** Each possible value must be formatted as backtick-delimited code followed by a colon and a description. Multiple values are separated by `<br>` within the cell.
**Wrong:**
```md
Values: 0, 1, or 2
```
**Right:**
```md
`0`: Does nothing <br> `1`: Does something <br> `2`: Does something else
```
**Source:** ROCm custom

---

## Rule: ENV-006
**Severity:** warning
**Scope:** Environment variable tables — default value column omission
**Rule:** The "Default value" column may be omitted only if all variables in that table are unset by default. When omitted, a note must be added under the category heading stating that the variables are unset by default.
**Wrong:**
```md
## Debug variables

Environment variable | Values
---------------------|-------
`DEBUG_FLAG` <br> Enables debug mode. | `0`: Off <br> `1`: On
```
(Default column omitted but no explanatory note.)
**Right:**
```md
## Debug variables

These variables control debug behavior. They are all unset by default.

Environment variable | Values
---------------------|-------
`DEBUG_FLAG` <br> Enables debug mode. | `0`: Off <br> `1`: On
```
**Source:** ROCm custom

---

## Rule: ENV-007
**Severity:** warning
**Scope:** Environment variable tables — complex defaults
**Rule:** When default values vary by architecture or require extended explanation, omit the "Default value" column and document the default inline at the end of the Values cell, prefixed with "Default:".
**Wrong:**
```md
Environment variable | Default value | Values
---------------------|---------------|-------
`MY_VAR` <br> Selects compiler. | `thing3` (except on z) | `thing3`: for x and y <br> `thing4`: for z
```
**Right:**
```md
Environment variable | Values
---------------------|-------
`MY_VAR` <br> Selects compiler. | `thing3`: for x and y <br> `thing4`: for z <br> Default: <br> `thing3` on x and y <br> `thing4` on z.
```
**Source:** ROCm custom

---

## Rule: ENV-008
**Severity:** warning
**Scope:** Environment variable tables — examples
**Rule:** When a variable accepts a file path or complex value, include a concrete usage example in the Values cell, formatted as: `Example: \`VAR_NAME=value\``.
**Wrong:**
```md
`filepath`: Prints to file
```
(No example of actual usage.)
**Right:**
```md
`filepath`: Does the thing and prints to file <br> Example: `YOUR_ENV_VAR=here/thisfile.txt`
```

```routing
tier: hybrid
applies_when: [env_var_shape]
strategy: structural
section_scope: true
note: Path/complex value detection is Script; adequacy of example is LLM.
```

**Source:** ROCm custom
