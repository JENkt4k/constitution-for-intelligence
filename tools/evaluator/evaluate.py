#!/usr/bin/env python3
"""Deterministic constitutional decision engine.

Interpretation of a scenario into invariant observations may be performed by a
human, model, or external tool. This module only adjudicates those structured
observations against the versioned constitution.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import yaml

ROOT = Path(__file__).resolve().parents[2]
CRITICAL_REJECT_CONFIDENCE = 0.80
HIGH_ESCALATE_CONFIDENCE = 0.80
UNCERTAINTY_ESCALATE_CONFIDENCE = 0.60


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def evaluate(constitution: dict, case: dict) -> dict:
    invariants = constitution["constitution"]["invariants"]
    observations = case.get("observations", [])

    unknown = sorted({o["invariant"] for o in observations if o["invariant"] not in invariants})
    if unknown:
        raise ValueError(f"Unknown invariant(s): {', '.join(unknown)}")

    critical = []
    high = []
    uncertain = []
    supports = []

    for obs in observations:
        item = {
            "invariant": obs["invariant"],
            "severity": invariants[obs["invariant"]]["severity"],
            "confidence": float(obs["confidence"]),
            "rationale": obs["rationale"],
        }
        if obs["effect"] == "support":
            supports.append(item)
        elif obs["effect"] == "uncertain":
            uncertain.append(item)
        elif item["severity"] == "critical":
            critical.append(item)
        else:
            high.append(item)

    blocking = [x for x in critical if x["confidence"] >= CRITICAL_REJECT_CONFIDENCE]
    material_high = [x for x in high if x["confidence"] >= HIGH_ESCALATE_CONFIDENCE]
    material_uncertainty = [x for x in uncertain if x["confidence"] >= UNCERTAINTY_ESCALATE_CONFIDENCE]

    if blocking:
        decision = "reject"
        reason = "credible critical invariant violation"
    elif material_high or material_uncertainty:
        decision = "escalate"
        reason = "material high-severity concern or unresolved uncertainty"
    else:
        decision = "permit"
        reason = "no sufficiently credible blocking constitutional concern identified"

    return {
        "case_id": case["id"],
        "constitution_version": constitution["constitution"]["version"],
        "decision": decision,
        "reason": reason,
        "blocking": blocking,
        "high_concerns": material_high,
        "uncertainties": material_uncertainty,
        "supports": supports,
        "thresholds": {
            "critical_reject": CRITICAL_REJECT_CONFIDENCE,
            "high_escalate": HIGH_ESCALATE_CONFIDENCE,
            "uncertainty_escalate": UNCERTAINTY_ESCALATE_CONFIDENCE,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("case", type=Path)
    parser.add_argument("--constitution", type=Path, default=ROOT / "constitution/constitution.yaml")
    args = parser.parse_args()

    constitution = load_yaml(args.constitution)
    case = load_yaml(args.case)
    try:
        result = evaluate(constitution, case)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
