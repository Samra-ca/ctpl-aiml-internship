"""
File: 05_safe_read_file.py

Demonstrates safe file reading using
proper exception handling.
"""


def safe_read_file(filepath):
    """
    Safely read a file.

    Args:
        filepath (str): Path of the file.
    """

    try:

        with open(filepath, "r") as file:

            content = file.read()

            if not content.strip():

                print("Warning: The file is empty.")

            else:

                print("\nFile Content:\n")
                print(content)

    except FileNotFoundError:

        print(
            "Error: The file you requested "
            "was not found. Please check the path."
        )

    except PermissionError:

        print(
            "Error: Permission denied."
        )

    except Exception as error:

        print(
            f"Unexpected Error: {error}"
        )


safe_read_file("sample_file.txt")