"""
Calculate statistics.
"""

import numpy as np

numbers = np.random.randint(
    1,
    101,
    20
)

print("Mean:", np.mean(numbers))
print("Median:", np.median(numbers))
print("Standard Deviation:", np.std(numbers))
print("Minimum:", np.min(numbers))
print("Maximum:", np.max(numbers))