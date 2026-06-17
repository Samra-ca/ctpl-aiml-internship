"""
Merge datasets.
"""

import pandas as pd

titanic = pd.read_csv(
    "../data/titanic.csv"
)

department = pd.read_csv(
    "../data/department_info.csv"
)

merged_df = pd.merge(
    titanic,
    department,
    on="Pclass",
    how="left"
)

print(
    merged_df.head()
)