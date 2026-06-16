"""
File: 02_student_management.py

Demonstrates:
1. Creating multiple objects
2. Working with instance attributes
"""


class Student:
    """
    Represents a student.
    """

    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def display_details(self):
        """Display student details."""
        print(
            f"ID: {self.student_id} | "
            f"Name: {self.name} | "
            f"Grade: {self.grade}"
        )


student1 = Student(101, "Ali", "A")
student2 = Student(102, "Sara", "A+")
student3 = Student(103, "Ahmed", "B+")

student1.display_details()
student2.display_details()
student3.display_details()