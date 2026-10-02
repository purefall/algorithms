"""Run only AFTER your manual dry-run. Default checks attempt.py."""
import importlib.util
from pathlib import Path
import sys
import unittest
MODULE = "solution" if "--solution" in sys.argv else "attempt"
if "--solution" in sys.argv: sys.argv.remove("--solution")
spec=importlib.util.spec_from_file_location(MODULE, Path(__file__).with_name(MODULE+".py"))
module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
class Cases(unittest.TestCase):
    def test_examples_and_edges(self):
        self.assertEqual(module.solve(*([3, 1, 5, 5, 2], 2)), 5)
        self.assertEqual(module.solve(*([1], 2)), None)
        self.assertEqual(module.solve(*([], 1)), None)
if __name__=="__main__": unittest.main()
