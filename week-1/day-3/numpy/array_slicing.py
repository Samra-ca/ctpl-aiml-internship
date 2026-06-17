"""
Array slicing example.
"""

import numpy as np

numbers = np.random.randint(
    1,
    101,
    20
).reshape(4, 5)

print(
    "First Two Rows:\n"
)

print(numbers[:2])