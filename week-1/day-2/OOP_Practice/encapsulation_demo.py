"""
File: 04_encapsulation_demo.py

Demonstrates:
1. Encapsulation
2. Protected attributes
"""


class Employee:
    """
    Employee information.
    """

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def get_salary(self):
        """Return employee salary."""
        return self._salary


employee = Employee(
    "Ahmed",
    75000
)

print(
    f"Employee Name: {employee.name}"
)

print(
    f"Salary: {employee.get_salary()}"
)