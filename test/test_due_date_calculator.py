import unittest
from src.calculator.due_date_calculator import dueDateCalculator


class TestDueDateCalculator(unittest.TestCase):
    def test_get_workhours(self):
        self.assertEqual(dueDateCalculator("2021-07-05 14:00", 5).get_workhours(), 11)
        self.assertEqual(dueDateCalculator("2021-07-05 11:00", 5).get_workhours(), 16)

    def test_weekday_add(self):
        self.assertEqual(
            dueDateCalculator("2021-07-09 14:00", 5).weekday_add(), "2021-07-12 11:00"
        )
        self.assertEqual(
            dueDateCalculator("2021-07-08 11:00", 5).weekday_add(), "2021-07-08 16:00"
        )


if __name__ == "__main__":
    unittest.main()
