"""
Reshape arrays.
"""

import numpy as np

numbers = np.random.randint(
    1,
    101,
    20
)

matrix = numbers.reshape(4, 5)

print(matrix)