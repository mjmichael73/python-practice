def sqrt(number: int | float) -> float:
    return number ** 0.5

if __name__ == "__main__":
    sqrt9 = sqrt(9)
    print(f"{sqrt9 = }")
    sqrt16 = sqrt(16.0)
    print(f"{sqrt16 = }")