monitor_size = 24
str_v = ""

match monitor_size:
    case 14 | 15:
        str_v = "too small"
    case x if 16 <= x <= 18:
        str_v = "good for past decade"
    case x if 19 <= x <= 23:
        str_v = "for office work"
    case x if 24 <= x <= 27:
        str_v = "great choice"

print(f"{str_v=}")