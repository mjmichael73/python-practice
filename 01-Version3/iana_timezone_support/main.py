from datetime import datetime
from zoneinfo import ZoneInfo

def print_datetime():
    dt = datetime(2024, 11, 9, tzinfo=ZoneInfo("Europe/Moscow"))
    print(dt)

if __name__ == "__main__":
    print_datetime()