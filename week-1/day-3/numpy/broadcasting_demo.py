"""
Broadcasting example.
"""

import numpy as np

numbers = np.random.randint(
    1,
    101,
    20
).reshape(4, 5)

result = numbers * 2

print(result)