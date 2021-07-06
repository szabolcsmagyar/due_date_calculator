import unittest
from src.validator.submit_date_validator import submitDateValidator


class TestSubmitDate(unittest.TestCase):
    def test_is_valid_format_valid(self):
        self.assertTrue(submitDateValidator("2021-07-05 14:00", None).is_valid_format())

    def test_is_valid_format_valid_wo_hours(self):
        self.assertTrue(submitDateValidator("2021-07-05", None).is_valid_format())

    def test_is_valid_format_invalid(self):
        self.assertRaises(ValueError, submitDateValidator.is_valid_format, "2021/07/05")

    def test_submit_date_dt(self):
        self.assertEqual(
            submitDateValidator("2021-07-05 14:00", None).submit_date_dt(),
            (2021, 7, 5, 14, 0),
        )

    def test_is_weekday(self):
        self.assertEqual(submitDateValidator("2021-07-05 14:00", None).is_weekday(), 1)
        self.assertEqual(submitDateValidator("2021-07-04 14:00", None).is_weekday(), 0)

    def test_is_working_hours(self):
        self.assertEqual(submitDateValidator("2021-07-05 14:00").is_working_hours(), 1)
        self.assertEqual(submitDateValidator("2021-07-04 00:00").is_working_hours(), 0)

    def test_validator(self):
        self.assertRaises(ValueError, submitDateValidator.validator, "2021-07-05")
        self.assertRaises(ValueError, submitDateValidator.validator, "2021-07-04 12:00")


if __name__ == "__main__":
    unittest.main()
