import calendar
from datetime import datetime
from typing import List, Tuple

YEAR = 2024
MONTH = 2


class Workdays:
    first_day = 1
    last_day_of_the_month = calendar.monthrange(year=YEAR, month=MONTH)[1] + 1
    worked_days: List[datetime] = []

    def __init__(self, HOLYDAYS: Tuple[int, ...]) -> None:
        self.HOLYDAYS = HOLYDAYS
        self.exclude_sundays_and_holydays()

    def exclude_sundays_and_holydays(self) -> List[datetime]:
        for day in range(self.first_day, self.last_day_of_the_month):

            current_date = datetime(year=YEAR, month=MONTH, day=day)

            if current_date.weekday() != calendar.SUNDAY and day not in self.HOLYDAYS:
                self.worked_days.append(current_date)

        return self.worked_days
