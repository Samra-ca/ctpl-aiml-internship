"""
File: 01_text_file_read_write.py

Demonstrates reading and writing text files.
"""

with open(
    "internship_notes.txt",
    "r",
    encoding="utf-8"
) as file:

    content = file.read()

print("Original Content:\n")
print(content)

with open(
    "internship_notes.txt",
    "a",
    encoding="utf-8"
) as file:

    file.write(
        "\n\nPractice completed successfully."
    )

print(
    "\nNew line added successfully."
)