from ulab import numpy as np

array = np.array([
    [3, 7, 1],
    [10, 3, 2],
    [5, 6, 7]
])
print(array)
print()

# Sort the whole array
print(np.sort(array, axis=None))

# Sort along each row
print(np.sort(array, axis=1))

# Sort along each column
print(np.sort(array, axis=0))

