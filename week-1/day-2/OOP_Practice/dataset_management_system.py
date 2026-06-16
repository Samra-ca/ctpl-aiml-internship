"""
File: 05_dataset_management_system.py

Mini OOP project for dataset management.
"""


class DatasetProfile:
    """
    Base dataset class.
    """

    def __init__(self, file_name, description):
        self.file_name = file_name
        self.description = description

    def show_info(self):
        print(f"\nDataset: {self.file_name}")
        print(f"Description: {self.description}")


class CSVDataset(DatasetProfile):
    """
    CSV dataset class.
    """

    def __init__(
        self,
        file_name,
        description,
        rows,
        columns
    ):
        super().__init__(
            file_name,
            description
        )

        self.rows = rows
        self.columns = columns

    def display_summary(self):
        print(f"Rows: {self.rows}")
        print(f"Columns: {self.columns}")


dataset1 = CSVDataset(
    "sales.csv",
    "Monthly sales records",
    1500,
    12
)

dataset2 = CSVDataset(
    "customers.csv",
    "Customer information",
    2500,
    8
)

dataset1.show_info()
dataset1.display_summary()

dataset2.show_info()
dataset2.display_summary()