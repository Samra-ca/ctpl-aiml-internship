"""
File: 03_type_error_demo.py

Demonstrates TypeError handling.
"""

try:
    number = 100
    text = "50"

    result = number + text

    print(result)

except TypeError:
    print("Error: Cannot add integer and string.")