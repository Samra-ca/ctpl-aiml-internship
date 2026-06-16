"""
File: 02_value_error_demo.py

Demonstrates ValueError handling.
"""

try:
    age = int(input("Enter your age: "))

    print(f"Your age is {age}")

except ValueError:
    print("Error: Please enter a valid integer.")