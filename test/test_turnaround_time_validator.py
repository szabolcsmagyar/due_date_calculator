import unittest
from src.validator.turnaround_time_validator import turnaroundTimeValidator


class TestTurnaroundTime(unittest.TestCase):
    def test_is_number(self):
        self.assertTrue(turnaroundTimeValidator(None, 5).is_number())
        self.assertFalse(turnaroundTimeValidator(None, iamanobject).is_number())
        self.assertTrue(turnaroundTimeValidator(None, "not").is_number())

    def test_validator(self):
        self.assertRaises(ValueError, turnaroundTimeValidator.validator, iamanobject)
        self.assertRaises(ValueError, turnaroundTimeValidator.validator, "not")


if __name__ == "__main__":
    unittest.main()
