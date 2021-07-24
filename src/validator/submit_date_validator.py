from datetime import datetime

class submitDateValidator:
    def __init__(self, submit_date):
        self.submit_date = submit_date
        self.submit_date_dt = None
        self.date_format = None

    def is_valid_format(self):
        valid_formats = ["%Y-%m-%d %H:%M", "%d/%m/%Y %H:%M"]

        for format_ in valid_formats:
            if datetime.strptime(self.submit_date, format_):
                self.date_format = format_
                return True
        raise ValueError(f"Invalid format. Valid formats are: {valid_formats}")

    def set_submit_date_dt(self):
        if self.is_valid_format():
            self.submit_date_dt = datetime.strptime(self.submit_date, self.date_format)

    def is_weekday(self):
        return 1 if self.submit_date_dt.isoweekday() in range(1, 6) else 0

    def is_working_hours(self):
        return 1 if self.submit_date_dt.hour in range(9, 18) else 0

    def validator(self):
        # Convert string to datetime
        self.set_submit_date_dt()

        if not self.is_weekday():
            raise ValueError("Submit date is not valid due to not being a weekday")

        if not self.is_working_hours():
            raise ValueError(
                "Submit date is not valid due to not being a working hours"
            )

        return self.submit_date_dt
