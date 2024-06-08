# code to be run in micropython

from ulab import numpy as np

a = np.array([1, 2, 3, 4, 5])
print("a: \t", a)
print("a flipped:\t", np.flip(a))

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.uint8)
print("\na flipped horizontally\n", np.flip(a, axis=1))
print("\na flipped vertically\n", np.flip(a, axis=0))
print("\na flipped horizontally+vertically\n", np.flip(a))

