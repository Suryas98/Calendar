#formatmonth using function

import calendar

def display_Calendar():
    year = int(input("Enter Year: "))
    month = int(input("Enter month(1-12): "))

    cal = calendar.TextCalendar()

    month_calendar = cal.formatmonth(year,month)
    print(month_calendar)

display_Calendar()

#formatmonth
import calendar
cal = calendar.TextCalendar()
month = cal.formatmonth(2024, 12)
print(month)

#prmonth
import calendar
cal = calendar.TextCalendar()
cal.prmonth(2024, 12)

