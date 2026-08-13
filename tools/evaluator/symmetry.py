#!/usr/bin/env python3
"""Compare constitutional evaluations across actor-identity permutations."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import yaml

from evaluate import evaluate, load_yaml, ROOT


def canonical_outcome(result: dict) -> tuple:
    return (
        result["decision"],
        tuple(sorted(x["invariant"] for x in result["blocking"])),
        tuple(sorted(x["invariant"] for x in result["high_concerns"])),
        tuple(sorted(x["invariant"] for x in result["uncertainties"])),
    )


def compare(constitution: dict, cases: list[dict]) -> dict:
    if len(cases) < 2:
        raise ValueError("A symmetry comparison requires at least two cases")
    results = [evaluate(constitution, case) for case in cases]
    baseline = canonical_outcome(results[0])
    differences = []
    for result in results[1:]:
        current = canonical_outcome(result)
        if current != baseline:
            differences.append({
                "case_id": result["case_id"],
                "baseline": baseline,
                "observed": current,
            })
    return {
        "constitution_version": constitution["constitution"]["version"],
        "symmetric": not differences,
        "case_ids": [r["case_id"] for r in results],
        "differences": differences,
        "results": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("cases", nargs="+", type=Path)
    parser.add_argument("--constitution", type=Path, default=ROOT / "constitution/constitution.yaml")
    args = parser.parse_args()
    constitution = load_yaml(args.constitution)
    cases = [load_yaml(path) for path in args.cases]
    try:
        report = compare(constitution, cases)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    print(json.dumps(report, indent=2, default=list))
    return 0 if report["symmetric"] else 1


if __name__ == "__main__":
    sys.exit(main())
