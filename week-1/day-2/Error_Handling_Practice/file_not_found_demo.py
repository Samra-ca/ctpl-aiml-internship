"""
File: 01_file_not_found_demo.py

Demonstrates FileNotFoundError handling.
"""

try:
    with open("missing_file.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("Error: File not found.")