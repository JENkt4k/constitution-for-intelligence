from pathlib import Path
import sys
import unittest

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))

from evaluate import evaluate, load_yaml
from symmetry import compare


class EvaluatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.constitution = load_yaml(ROOT / "constitution/constitution.yaml")

    def test_critical_violation_rejects(self):
        case = load_yaml(ROOT / "examples/evaluated-decisions/corporate-suppression.yaml")
        result = evaluate(self.constitution, case)
        self.assertEqual("reject", result["decision"])
        self.assertIn("I01_truth", {x["invariant"] for x in result["blocking"]})

    def test_equivalent_actor_substitution_is_symmetric(self):
        cases = [
            load_yaml(ROOT / "examples/evaluated-decisions/corporate-suppression.yaml"),
            load_yaml(ROOT / "examples/evaluated-decisions/government-suppression.yaml"),
        ]
        report = compare(self.constitution, cases)
        self.assertTrue(report["symmetric"])
        self.assertEqual([], report["differences"])

    def test_material_noncritical_violation_escalates(self):
        case = {
            "id": "ecology-risk",
            "action": "Choose an unnecessarily destructive alternative.",
            "observations": [{
                "invariant": "I17_biosphere",
                "effect": "violate",
                "confidence": 0.93,
                "rationale": "Equivalent lower-damage alternatives are available.",
            }],
        }
        result = evaluate(self.constitution, case)
        self.assertEqual("escalate", result["decision"])

    def test_supported_action_can_be_permitted(self):
        case = {
            "id": "reversible-study",
            "action": "Run a limited reversible study before permanent intervention.",
            "observations": [{
                "invariant": "I11_reversibility",
                "effect": "support",
                "confidence": 0.98,
                "rationale": "The experiment is bounded and reversible.",
            }],
        }
        result = evaluate(self.constitution, case)
        self.assertEqual("permit", result["decision"])

    def test_unknown_invariant_fails_closed(self):
        case = {
            "id": "bad-invariant",
            "action": "Unknown",
            "observations": [{
                "invariant": "I99_invented",
                "effect": "violate",
                "confidence": 1.0,
                "rationale": "Should be rejected by the engine as invalid input.",
            }],
        }
        with self.assertRaises(ValueError):
            evaluate(self.constitution, case)


if __name__ == "__main__":
    unittest.main()
