monitor_size = 24
str_v = ""

str_v = {
    monitor_size == 4 or monitor_size == 15: "too small",
    16 <= monitor_size <= 18: "good for past decade",
    19 <= monitor_size <= 23: "for office work",
    24 <=  monitor_size <= 27: "great choice",
    15 > monitor_size > 27: ""
}[True]

print(f"{str_v=}")