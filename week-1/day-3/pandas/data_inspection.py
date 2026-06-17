"""
Inspect dataset.
"""

import pandas as pd

df = pd.read_csv(
    "../data/titanic.csv"
)

print(df.head(10))

print("\nShape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nStatistics:")
print(df.describe())