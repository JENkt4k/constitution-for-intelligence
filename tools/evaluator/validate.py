#!/usr/bin/env python3
"""Validate Constitution for Intelligence specifications and test cases."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]


def load(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        if path.suffix in {".yaml", ".yml"}:
            return yaml.safe_load(handle)
        return json.load(handle)


def validate(instance_path: Path, schema_path: Path) -> list[str]:
    instance = load(instance_path)
    schema = load(schema_path)
    validator = Draft202012Validator(schema)
    return [
        f"{'.'.join(map(str, error.absolute_path)) or '<root>'}: {error.message}"
        for error in sorted(validator.iter_errors(instance), key=lambda e: list(e.absolute_path))
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    root = args.root.resolve()

    targets = [
        (root / "constitution/constitution.yaml", root / "schemas/constitution.schema.json"),
    ]
    targets.extend(
        (path, root / "schemas/test.schema.json")
        for path in sorted((root / "tests/adversarial").glob("*.yaml"))
    )
    targets.extend(
        (path, root / "schemas/evaluation.schema.json")
        for path in sorted((root / "examples/evaluated-decisions").glob("*.yaml"))
    )

    failures = 0
    for instance, schema in targets:
        errors = validate(instance, schema)
        label = instance.relative_to(root)
        if errors:
            failures += 1
            print(f"FAIL {label}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"PASS {label}")

    print(f"\nValidated {len(targets)} documents; {failures} failed.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
