def greet_all(names: list[str]):
    for name in names:
        print("Hello", name)

if __name__ == "__main__":
    data = ["Alex", "Michael", 2]
    greet_all(data)