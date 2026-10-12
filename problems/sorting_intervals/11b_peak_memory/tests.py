"""Run only AFTER your manual dry-run. Checks attempt.py."""

import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location("attempt", Path(__file__).with_name("attempt.py"))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class Cases(unittest.TestCase):
    def test_examples_and_edges(self):
        self.assertEqual(module.solve([(1, 5, 2), (3, 8, 4), (4, 6, 3)]), (9, (4, 5)))
        self.assertEqual(module.solve([(0, 3, 1), (0, 3, 1), (0, 3, 1), (5, 6, 4)]), (4, (5, 6)))
        self.assertEqual(module.solve([(1, 4, 5), (4, 6, 5)]), (5, (1, 6)))
        self.assertEqual(module.solve([(1, 4, 5), (4, 6, 3)]), (5, (1, 4)))
        self.assertEqual(module.solve([]), (0, None))
        self.assertEqual(module.solve([(1, 3, 2), (3, 5, 1), (3, 5, 1)]), (2, (1, 5)))
        self.assertEqual(module.solve([(1, 3, 2), (5, 7, 2)]), (2, (1, 3)))
        self.assertEqual(module.solve([(2, 2, 100), (1, 3, 1)]), (1, (1, 3)))
        self.assertEqual(module.solve([(6, 9, 3), (2, 4, 1)]), (3, (6, 9)))


if __name__ == "__main__":
    unittest.main()
