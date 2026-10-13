<!--
Regression fixture for checks that were turned off because they misfired on
ROCm documentation or contradict ROCm policy. Run:
`vale --config=vale/.vale.ini vale/testdata/disabled-checks.md`

Expected findings: exactly 1, and it is ROCm.CORE-024 on the final line
("in order to"), kept so this fixture proves the rule set is still running.
Every other line below must produce NO finding. Before the change each of
these fired:
  line "click"              Microsoft.UIVerbs      (a mouse action is not meant here)
  line "punctuation"        Microsoft.Quotes       (technical text quotes exactly)
  line "URL"                Microsoft.GeneralURL   (readers are technical)
  line "numerical"          Microsoft.Terms        ("numerical methods" is correct)
  line "pre- and post-"     Microsoft.Suspended
  line "e.g."               Microsoft.Foreign      (e.g. and i.e. are allowed)
  line "multiply-add"       Google.LyHyphens       (matches any word ending in -ly)
  line "only-if-needed"     Google.LyHyphens
  line "Si Si" / "7.x.x"    Vale.Repetition        (a name, and a version)
  line "v3" / "v1.5"        ROCm.CORE-022          (standard names; rule suspended)
  line "above"              ROCm.CORE-024          (rules/03 uses "listed above" as a Right example)
  line "functionality"      ROCm.CORE-024
  line "open-source"        ROCm.CORE-024          (SPELL-006 defers it to human judgment)
  line "abort"              ROCm.CORE-024
  line "SHA1"               ROCm.CORE-024          (suggested the nonsense "HAS-SHA1")
  line "simple"/"please"    ROCm.SPELL-009
  line "easy"/"easily"      ROCm.SPELL-009
-->

# Disabled checks

Single click to run interaction models is supported in this release.

Use "quoted phrase", then another "one".

Open the serving URL in the browser.

It might differ in performance or numerical behavior.

The image is pre- and post-processed for each frame.

Include models such as UNet (e.g., UNETR) and the standard names (i.e., the defaults).

The fused multiply-add instruction is used, with only-if-needed upgrades.

Authors are Huan Zhang, Si Si and Cho-Jui Hsieh. This applies to ROCm 7.x.x releases.

The OHIF v3 viewer, Inception v3 and PKCS#1 v1.5 padding are used.

See the table above for the open-source library functionality, or abort the run.

The commit hash is the latest SHA1 of the HEAD branch.

This is a simple step. Please run the step. The step is easy and runs easily.

Done in order to speed up later runs.
