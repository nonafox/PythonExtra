# code to be run in micropython

from ulab import numpy as np

x = np.linspace(0, 10, num=1024)
y = np.sin(x)
z = np.zeros(len(x))

a, b = np.fft.fft(x)
print('real part:\t', a)
print('\nimaginary part:\t', b)

c, d = np.fft.fft(x, z)
print('\nreal part:\t', c)
print('\nimaginary part:\t', d)


