class Employee:
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position
    
    def __repr__(self) -> str:
        return (
            "Employy(name='{}', salary='{}', position='{}')".format(self.name, self.salary, self.position)
        )
    
    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return (self.name, self.salary) == (other.name, other.salary)
        return NotImplemented
    
    def __ne__(self, other):
        if other.__class__ is self.__class__:
            return (self.name, self.salary) != (other.name, other.salary)
        return NotImplemented
    
    def __le__(self, other):
        if other.__class__ is self.__class__:
            return (self.name, self.salary) <= (other.name, other.salary)
        return NotImplemented
    
    def __lt__(self, other):
        if other.__class__ is self.__class__:
            return (self.name, self.salary) < (other.name, other.salary)
        return NotImplemented
    
    def __gt__(self, other):
        if other.__class__ is self.__class__:
            return (self.name, self.salary) > (other.name, other.salary)
        return NotImplemented

    def __ge__(self, other):
        if other.__class__ is self.__class__:
            return (self.name, self.salary) >= (other.name, other.salary)
        return NotImplemented

alex1 = Employee(name="Alex1", salary=3000, position="manager")
alex2 = Employee(name="Alex2", salary=5000, position="director")

print(alex1 == alex2)
print(alex1 <= alex2)
print(alex1 < alex2)
print(alex1 >= alex2)
print(alex1 > alex2)
print(alex1 != alex2)