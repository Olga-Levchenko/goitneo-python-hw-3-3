from collections import defaultdict
from datetime import datetime
from datetime import timedelta

weekdays = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thurday",
    4: "Friday"
}

def get_birthdays_per_week(users):
    birthdays_this_week = defaultdict()
    for weekday in weekdays.values():        
        birthdays_this_week[weekday] = []
    today = datetime.today().date()
    next_monday = today
    while next_monday.weekday() != 0:
        next_monday = next_monday + timedelta(days=1)
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        # Note: I don't increment the year in the case when birthday date has already passed in this year because with this condition
        # it is hard to implement acceptance criteria 1 "Користувачів, у яких день народження був на вихідних, потрібно привітати в понеділок." neatly.
        delta_days = (birthday_this_year - today).days
        if delta_days >= -2 and delta_days <= 5:
            congratulate_on = birthday_this_year.weekday()
            if congratulate_on >= 5:
                congratulate_on = 0
            day_of_week = weekdays[congratulate_on]
            day_of_week_birthday_list = birthdays_this_week[day_of_week]
            day_of_week_birthday_list.append(name)
    weekdays_with_birthdays = list()    
    for weekday in weekdays.values():
        birthdays = birthdays_this_week[weekday]
        if len(birthdays) == 0:
            continue
        weekdays_with_birthdays.append(f"{weekday}: {', '.join(birthdays).rstrip()}")
    return "\n".join(weekdays_with_birthdays)

'''
#Example:
employees = [
    {"name": "Harry Potter", "birthday": datetime(1955, 10, 21)},
    {"name": "Croockshanks", "birthday": datetime(1955, 10, 22)},
    {"name": "Tom Riddle", "birthday": datetime(1955, 10, 23)},
    {"name": "Hermione Granger", "birthday": datetime(1955, 10, 24)},
    {"name": "Ron Wisley", "birthday": datetime(1955, 10, 25)},
    {"name": "Loona Lovegood", "birthday": datetime(1955, 10, 26)},
    {"name": "Nevill Longbottom", "birthday": datetime(1955, 10, 27)},
    {"name": "Minerva Macgonagal", "birthday": datetime(1955, 10, 28)},
    {"name": "Severus Snape", "birthday": datetime(1955, 10, 29)},
    {"name": "Albus Dumbldore", "birthday": datetime(1955, 10, 30)},
]
get_birthdays_per_week(employees)
'''