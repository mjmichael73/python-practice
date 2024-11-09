from zoneinfo import ZoneInfo
from datetime import datetime

dt = datetime(2021, 2, 17, 12, tzinfo=ZoneInfo("Europe/Moscow"))
print(dt)