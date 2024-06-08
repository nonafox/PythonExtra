# code to be run in micropython

from ulab import numpy as np

a = np.array([1, 2, 3, 4], dtype=np.uint8)
b = np.array([1+1j, 2-2j, 3+3j, 4-4j], dtype=np.complex)

print('a:\t\t', a)
print('conjugate(a):\t', np.conjugate(a))
print()
print('b:\t\t', b)
print('conjugate(b):\t', np.conjugate(b))


