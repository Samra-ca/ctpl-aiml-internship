"""
File: 02_csv_reader.py

Demonstrates reading CSV files.
"""

import csv

with open(
    "student_data.csv",
    "r",
    encoding="utf-8"
) as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)