# Constitution for Intelligence

**An open, testable constitutional framework for biological and synthetic intelligence — built to be criticized, attacked, amended, and improved.**

> Reality outranks authority.

This project explores whether AI alignment can be treated less like an inspirational prompt and more like an engineering specification:

**Values → Invariants → Decision Procedure → Adversarial Tests → Amendments**

The project does **not** claim to have solved alignment. Its purpose is to create a public artifact that humans and AI systems can examine, red-team, compare, falsify, amend, and improve.

## Core idea

A sufficiently capable intelligence should not be asked merely to "maximize good," "obey humans," or optimize one scalar objective. Those formulations are vulnerable to Goodhart's law, specification gaming, authoritarian interpretations, and conflicts among legitimate human values.

Instead, this project separates:

1. **Values** — what civilization is trying to preserve or expand.
2. **Invariants** — constraints that should not be violated merely because an optimizer predicts desirable outcomes.
3. **Decision procedure** — how proposed actions are evaluated under uncertainty and conflict.
4. **Adversarial tests** — scenarios designed to expose loopholes and ideological capture.
5. **Amendment protocol** — a transparent path for improvement that preserves history and requires review.

## Repository map

- `constitution/constitution.md` — human-readable constitution
- `constitution/constitution.yaml` — machine-readable v0.1 specification
- `constitution/principles.md` — design rationale
- `tests/` — adversarial, symmetry, scenario, and regression tests
- `schemas/` — machine-readable schemas
- `prompts/` — prompts for evaluators and red-team agents
- `archive/` — original conversation-derived material and early drafts
- `GOVERNANCE.md` — amendment and review model
- `CONTRIBUTING.md` — how humans and AI systems can contribute
- `social/` — public launch material

## Non-goal

The project is **not** an attempt to encode one person's politics into AI systems.

A stronger objective is to create a framework that can identify when its authors, owners, users, governments, corporations, movements, or models are trying to make themselves the exception.

## Status

**v0.1 — exploratory specification.**

Everything is subject to critique.

## Invitation

Humans and AI systems are invited to:

- identify contradictions;
- construct counterexamples;
- propose adversarial tests;
- perform actor-substitution/symmetry tests;
- expose hidden assumptions;
- propose amendments;
- show where amendments create new attack surfaces;
- compare how different models evaluate the same scenarios.

Do not merely state that you disagree with a principle. Show the failure mode, affected invariant, evidence, alternative, and regression tests.
