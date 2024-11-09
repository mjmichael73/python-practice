from dataclasses import dataclass, field

@dataclass(order=True)
class Employee:
    name: str
    salary: float
    position: str = field(compare=False)

Alex1 = Employee("Alex", 6000, "manager")
Alex2 = Employee("Alex", 5000, "director")

print(Alex1 < Alex2)