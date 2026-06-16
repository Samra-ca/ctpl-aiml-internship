"""
File: 03_inheritance_demo.py

Demonstrates:
1. Inheritance
2. Reusing parent class methods
"""


class Dataset:
    """
    Parent class.
    """

    def __init__(self, dataset_name):
        self.dataset_name = dataset_name

    def load_dataset(self):
        print(f"{self.dataset_name} loaded successfully.")


class CSVDataset(Dataset):
    """
    Child class inheriting Dataset.
    """

    def get_column_count(self):
        return 8


csv_data = CSVDataset("Sales Dataset")

csv_data.load_dataset()

print(
    f"Column Count: {csv_data.get_column_count()}"
)