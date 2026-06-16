"""
File: 01_dataset_profile.py

Demonstrates:
1. Class creation
2. Constructor (__init__)
3. Methods
4. Object creation
"""


class DatasetProfile:
    """
    Represents a dataset profile.
    """

    def __init__(self, file_name, description):
        """
        Initialize dataset details.

        Args:
            file_name (str): Dataset filename
            description (str): Dataset description
        """
        self.file_name = file_name
        self.description = description

    def load_info(self):
        """Display dataset information."""
        print(f"File Name : {self.file_name}")
        print(f"Description : {self.description}")

    def display_summary(self):
        """Display summary information."""
        print("Summary: Dataset contains information for analysis.")


dataset = DatasetProfile(
    "students.csv",
    "Student performance dataset"
)

dataset.load_info()
dataset.display_summary()