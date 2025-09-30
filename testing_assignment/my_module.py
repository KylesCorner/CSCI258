# my_module.py


def max3(a, b, c):
    return max(a, b, c)


def odd(a, b, c):
    return (a + b + c) % 2 == 1


def majority(a, b, c):
    return (a + b + c) >= 2


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Name: {self.name}, Salary: ${self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_details(self):
        return (
            f"Name: {self.name}, Salary: ${self.salary}, Department: {self.department}"
        )
