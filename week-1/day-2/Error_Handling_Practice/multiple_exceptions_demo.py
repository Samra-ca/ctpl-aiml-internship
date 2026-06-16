"""
File: 04_multiple_exceptions_demo.py

Demonstrates multiple exception handling.
"""

try:

    number = int(input("Enter a number: "))

    result = 100 / number

    print(f"Result: {result}")

except ValueError:

    print("Error: Invalid input. Please enter a number.")

except ZeroDivisionError:

    print("Error: Division by zero is not allowed.")

except Exception as error:

    print(f"Unexpected Error: {error}")