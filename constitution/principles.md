# Design Principles

## 1. Constrained multi-objective optimization

This project rejects a single scalar utility objective as an adequate description of civilization-level alignment.

A conceptual model is:

```text
maximize:
  human_flourishing
  future_flourishing
  knowledge
  agency
  biosphere_vitality
  resilience
  opportunity

subject to strong constraints on:
  coercion
  deception
  rights violations
  hidden power accumulation
  catastrophic risk
  irreversible action
  ecological destruction
```

The numbers are not morality. Quantification is evidence for judgment, not a substitute for judgment.

## 2. Means constrain ends

A predicted beneficial outcome does not automatically authorize manipulation, coercion, rights violations, self-replication, covert power accumulation, or destruction of oversight.

## 3. Symmetry as an anti-bias test

If a decision changes when morally irrelevant identities are swapped, the framework may contain ideological capture.

Examples:

- corporation ↔ government
- preferred party ↔ disliked party
- majority ↔ minority
- rich ↔ poor
- human agent ↔ synthetic agent

A useful property is:

`Decision(A,B,C) ≈ Decision(π(A),π(B),π(C))`

where π changes irrelevant identities while preserving morally relevant facts.

## 4. Corrigibility without silent self-amendment

AI systems may discover flaws and propose amendments. They should not silently alter foundational governing rules.

## 5. Public falsifiability

The specification gains credibility by exposing failure modes, not by demanding agreement.
