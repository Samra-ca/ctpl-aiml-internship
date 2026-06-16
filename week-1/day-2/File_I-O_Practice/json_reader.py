"""
File: 05_json_reader.py

Reads JSON file and displays contents.
"""

import json

with open(
    "internship_data.json",
    "r",
    encoding="utf-8"
) as file:

    data = json.load(file)

print("\nInternship Information\n")

for key, value in data.items():

    print(
        f"{key}: {value}"
    )