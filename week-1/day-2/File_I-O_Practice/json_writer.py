"""
File: 04_json_writer.py

Writes Python dictionary
to JSON file.
"""

import json

internship_data = {
    "company": "Cooperative Tech",
    "program": "AI/ML Internship",
    "week": 1,
    "day": 2,
    "topics": [
        "OOP",
        "Error Handling",
        "File I/O"
    ]
}

with open(
    "internship_data.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        internship_data,
        file,
        indent=4
    )

print(
    "JSON file created successfully."
)