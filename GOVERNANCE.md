# Governance

The Constitution for Intelligence is an experimental open specification.

## Amendment lifecycle

1. Identify a concrete defect, contradiction, exploit, or missing case.
2. Provide evidence or a reproducible scenario.
3. Identify affected invariants.
4. Propose the smallest sufficient amendment.
5. Describe expected benefit.
6. Describe new attack surface and possible harms.
7. Add adversarial tests.
8. Add symmetry tests where actor identity could matter.
9. Run regression tests against prior accepted cases.
10. Submit for public review.
11. Merge only through an explicit, recorded decision.
12. Version the resulting specification.

## Required amendment record

```yaml
amendment:
  problem:
  evidence:
  affected_invariants:
  proposed_change:
  expected_benefit:
  possible_harms:
  new_attack_surface:
  alternatives_considered:
  adversarial_tests:
  symmetry_tests:
  regression_tests:
```

## Constitutional changes

No AI system, maintainer, sponsor, institution, owner, or contributor is permitted by project convention to silently alter constitutional constraints.

## Governance goal

The governance model should itself be subject to the same questions as the constitution: Is power accountable, contestable, transparent, distributed, and reversible?
