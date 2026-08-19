---
title: "Write JUnit tests to cover all statements of `OrderSummary`"
labels: ["testing", "coverage", "statement-coverage"]
---

Task: Write JUnit tests that exercise every statement in `com.example.OrderSummary.calculateFinalScore`.

Acceptance Criteria:
- Add tests covering:
  - loop branch where score >= passMark
  - loop branch where score < passMark
  - final bonus branch where total >= 100
  - final non-bonus branch where total < 100
  - edge case: empty scores array

Assign to: @me
