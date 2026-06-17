"""
Data cleaning.
"""

import pandas as pd

df = pd.read_csv(
    "../data/titanic.csv"
)

print(
    df.isnull().sum()
)

df["Age"] = df["Age"].fillna(
    df["Age"].median()
)

df["Embarked"] = df["Embarked"].fillna(
    "Unknown"
)

df = df.drop_duplicates()

print(
    "\nAfter Cleaning:\n"
)

print(
    df.isnull().sum()
)