import datetime
import re


def conv_date(time_string: str):
    year, month, date = re.findall(r"\d+", time_string)
    return datetime.datetime.strptime(f"{year}-{month.zfill(2)}-{date}", "%Y-%m-%d")


def count_between_dt(day1: datetime.datetime, day2: datetime.datetime) -> (int, int):
    now = datetime.datetime.now()
    return (now - day1).days, (day2 - now).days


if __name__ == '__main__':
    start = conv_date(input("start of service: "))
    end = conv_date(input("end of service: "))

    served, left = count_between_dt(start, end)
    print(f"You served {served} days, {left} days to serve.")
