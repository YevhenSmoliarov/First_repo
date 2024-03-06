from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    today = datetime.today().date()
    current_day = today.weekday()

    birthdays = {i: [] for i in range(7)}

    for user in users:
        birthday = user["birthday"].date()

        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        birthday_weekday = (today + timedelta(days=delta_days)).weekday()

        if delta_days <= current_day:
            birthday_weekday = (birthday_weekday + 1) % 7

        birthdays[birthday_weekday].append(user["name"])


    for day, names in birthdays.items():
        day_name = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][day]
        if names:
            print(f"{day_name}: {', '.join(names)}")