def f_string_support():
    from datetime import datetime
    number = 42
    pi = 3.1415
    text = "answer"
    now = datetime.now()
    print("In version 3.8:")
    print(f"{number=}")
    print(f"{pi=}")
    print(f"{text=}")
    print(f"{now=}")

    print("Before:")
    print(f"number={number}")
    print(f"pi={pi}")
    print(f"text={text}")
    print(f"now={now}")

f_string_support()