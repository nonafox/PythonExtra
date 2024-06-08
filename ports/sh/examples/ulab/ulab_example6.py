# code to be run in micropython

from ulab import numpy as np

m = np.array([[1, 2, 3], [4, 5, 6], [7, 10, 9]], dtype=np.uint8)
n = np.linalg.inv(m)
print("m:\n", m)
print("\nm^-1:\n", n)
# this should be the unit matrix
print("\nm*m^-1:\n", np.dot(m, n))

m = np.array([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=np.uint8)
n = np.array([[1, 2], [3, 4], [5, 6], [7, 8]], dtype=np.uint8)
print(m)
print(n)
print(np.dot(m, n))
