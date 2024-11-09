def f_string_support():
    from datetime import datetime
    number = 42
    pi = 3.1415
    text = "answer"
    now = datetime.now()
    print(f"{number=}")
    print(f"{pi=}")
    print(f"{text=}")
    print(f"{now=}")

f_string_support()