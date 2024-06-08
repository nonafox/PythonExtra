# code to be run in micropython

from ulab import numpy as np

a = np.array([1, 2, 3], dtype=np.uint16)
print("a:\t\t", a)
print("imag(a):\t", np.imag(a))

b = np.array([1, 2+1j, 3-1j], dtype=np.complex)
print("\nb:\t\t", b)
print("imag(b):\t", np.imag(b))

    
