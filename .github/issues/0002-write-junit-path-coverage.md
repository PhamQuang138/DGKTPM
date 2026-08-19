---
title: "Write JUnit tests to cover all paths of `OrderSummary`"
labels: ["testing", "coverage", "path-coverage"]
---

Task: Write JUnit tests that aim to cover all control-flow paths through `calculateFinalScore`.

Notes:
- Full path coverage is exponential in the number of loop iterations; provide a representative set of tests that exercise distinct execution paths (single-element, multi-element with mixed branches, all-above, all-below, empty).
- Include tests that assert exact-bounds (e.g., score == passMark) and threshold behaviors.

Acceptance Criteria:
- Tests for single-element below/above
- Tests for multi-element mixtures that flip per-iteration branch
- Test for exact total == 100 (bonus applied)

Assign to: @me
