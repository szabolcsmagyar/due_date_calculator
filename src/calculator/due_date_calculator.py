from datetime import timedelta
from src.validator.submit_date_validator import submitDateValidator
from src.validator.turnaround_time_validator import turnaroundTimeValidator

class dueDateCalculator:
    def __init__(self, submit_date, turnaround_time):
        self.submit_date = submitDateValidator(submit_date).validator()
        self.turnaround_time = turnaroundTimeValidator(turnaround_time).validator()
        self.start_time = 9
        self.end_time = 17
        self.working_hours = self.end_time - self.start_time
        self.days_add = None
        self.hours_add = None

    def get_workhours(self):
        # Calculate how many hours need to be added to the working hours
        turnaround_time_hours_left = self.turnaround_time % self.working_hours

        # Calculate how many days need to be added
        self.days_add = self.turnaround_time // self.working_hours

        supposed_to_finish_working = self.submit_date.hour + turnaround_time_hours_left

        if supposed_to_finish_working > self.end_time:
            self.days_add += 1
            self.hours_add = (
                self.start_time + supposed_to_finish_working - self.end_time
            )
        else:
            self.hours_add = supposed_to_finish_working

        return self.days_add, self.hours_add

    def calculate_time(self):

        self.get_workhours()

        due_date = self.submit_date + timedelta(days=self.days_add)
        due_date = due_date.replace(hour=self.hours_add)

        if due_date.isoweekday() in [6, 7]:
            extra_days = 7 - due_date.isoweekday() + 1
            due_date = due_date + timedelta(extra_days)

        return due_date

    def run(self):
        return self.calculate_time()
