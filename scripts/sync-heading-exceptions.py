#!/usr/bin/env python3
"""Regenerate the proper-noun parts of the heading-case rules.

Source of truth: wordlists/heading-proper-nouns.txt

Generated regions (everything between the markers is overwritten):

  vale/styles/ROCm/CORE-008.yml     the `exceptions:` entries between the
                                    "BEGIN GENERATED" / "END GENERATED" comment
                                    lines (reStructuredText headings)
  vale/styles/ROCm/CORE-008-MD.yml  the alternation between the inline
                                    `(?#BEGIN-NOUNS)` and `(?#END-NOUNS)`
                                    regex comments (Markdown headings)

A list line may end with `@md` to mark a name as Markdown-only; it is then
left out of CORE-008.yml.

Usage:
  python scripts/sync-heading-exceptions.py           rewrite the rule files
  python scripts/sync-heading-exceptions.py --check   exit 1 if they are stale

Standard library only, so CI needs no extra installs.
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORDLIST = ROOT / "wordlists" / "heading-proper-nouns.txt"
RST_RULE = ROOT / "vale" / "styles" / "ROCm" / "CORE-008.yml"
MD_RULE = ROOT / "vale" / "styles" / "ROCm" / "CORE-008-MD.yml"

RST_REGION = re.compile(
    r"(?P<begin>^  # BEGIN GENERATED[^\n]*\n)(?P<body>.*?)(?P<end>^  # END GENERATED[^\n]*\n)",
    re.DOTALL | re.MULTILINE,
)
MD_REGION = re.compile(r"(?P<begin>\(\?#BEGIN-NOUNS\))(?P<body>.*?)(?P<end>\(\?#END-NOUNS\))", re.DOTALL)

# Characters that are special in a Vale (Go/.NET) regular expression.
REGEX_SPECIAL = set("\\.+*?()[]{}|^$")


def read_entries():
    """Return [(name, md_only)] in file order, without duplicates."""
    entries = []
    seen = set()
    for raw in WORDLIST.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        md_only = False
        if re.search(r"\s@md$", line):
            md_only = True
            line = line[: -len("@md")].rstrip()
        if line not in seen:
            seen.add(line)
            entries.append((line, md_only))
    if not entries:
        sys.exit(f"{WORDLIST}: no entries found")
    return entries


def regex_escape(text):
    return "".join("\\" + c if c in REGEX_SPECIAL else c for c in text)


def yaml_scalar(text):
    """Return `text` as a YAML scalar, single-quoted only when a plain one
    would be misread."""
    unsafe_start = text[0] in "-?:,[]{}#&*!|>'\"%@`" or text != text.strip()
    if unsafe_start or ": " in text or " #" in text or text.endswith(":"):
        return "'" + text.replace("'", "''") + "'"
    return text


def rst_body(entries):
    return "".join(
        f"  - {yaml_scalar(regex_escape(name))}\n" for name, md_only in entries if not md_only
    )


def md_alternatives(entries):
    """Regex alternatives that exempt a plain Capitalized word, but only where
    it sits inside the listed name.

    A single-word name becomes the bare word. A word inside a multi-word name
    becomes the word plus lookarounds for the rest of the name, so listing
    "GitHub Issues" exempts "Issues" after "GitHub" and not in "Resolved
    Issues". Only plain Capitalized words ([A-Z][a-z]+) are emitted: the
    Markdown rule can match no other token shape.
    """
    alternatives = []
    for name, _md_only in entries:
        for m in re.finditer(r"[A-Z][a-z]+", name):
            start, end = m.span()
            # Must be a whole token, not a slice of a camelCase or all-caps word.
            before = name[start - 1] if start else " "
            after = name[end] if end < len(name) else " "
            if before.isalnum() or after.isalnum():
                continue
            alt = m.group()
            if start:
                alt = f"(?<={regex_escape(name[:start])})" + alt
            if end < len(name):
                alt += f"(?={regex_escape(name[end:])})"
            if alt not in alternatives:
                alternatives.append(alt)
    return alternatives


def replace_region(text, pattern, body, path, what):
    matches = list(pattern.finditer(text))
    if len(matches) != 1:
        sys.exit(f"{path}: expected exactly one {what} region, found {len(matches)}")
    m = matches[0]
    return text[: m.start("body")] + body + text[m.end("body") :]


def render(entries):
    rst = RST_RULE.read_text(encoding="utf-8")
    md = MD_RULE.read_text(encoding="utf-8")
    new_rst = replace_region(rst, RST_REGION, rst_body(entries), RST_RULE, "BEGIN/END GENERATED")
    new_md = replace_region(md, MD_REGION, "|".join(md_alternatives(entries)), MD_RULE, "BEGIN-NOUNS/END-NOUNS")
    return {RST_RULE: (rst, new_rst), MD_RULE: (md, new_md)}


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--check", action="store_true", help="fail if the generated files are out of date")
    args = parser.parse_args()

    result = render(read_entries())
    stale = [path for path, (old, new) in result.items() if old != new]

    if args.check:
        if stale:
            names = ", ".join(str(p.relative_to(ROOT)) for p in stale)
            print(
                f"Out of date: {names}\n"
                "Run `python scripts/sync-heading-exceptions.py` and commit the result.",
                file=sys.stderr,
            )
            return 1
        print("Heading exception lists are in sync with wordlists/heading-proper-nouns.txt.")
        return 0

    for path in stale:
        path.write_text(result[path][1], encoding="utf-8", newline="\n")
        print(f"updated {path.relative_to(ROOT)}")
    if not stale:
        print("already up to date")
    return 0


if __name__ == "__main__":
    sys.exit(main())
