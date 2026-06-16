"""
File: 03_csv_to_text_converter.py

Reads student data and saves
selected information into a text file.
"""

import csv

with open(
    "student_data.csv",
    "r",
    encoding="utf-8"
) as csv_file:

    reader = csv.DictReader(csv_file)

    with open(
        "extracted_students.txt",
        "w",
        encoding="utf-8"
    ) as text_file:

        for row in reader:

            text_file.write(
                f"{row['Name']} - "
                f"{row['Department']}\n"
            )

print(
    "Student information extracted successfully."
)