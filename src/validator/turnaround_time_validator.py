from datetime import datetime

class turnaroundTimeValidator:
    def __init__(self, turnaround_time):
        self.turnaround_time = turnaround_time

    def is_number(self):
        return 1 if int(self.turnaround_time) else 0

    def is_positive_number(self):
        return 1 if int(self.turnaround_time) > 0 else 0

    def validator(self):
        if not self.is_number():
            raise ValueError("Turnaround time is not valid due to not being a number")

        if not self.is_positive_number():
            raise ValueError(
                "Turnaround time is not valid due to not being a positive number"
            )

        return self.turnaround_time
