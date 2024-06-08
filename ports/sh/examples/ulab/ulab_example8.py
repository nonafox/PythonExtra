# code to be run in micropython

from ulab import numpy as np
from ulab import scipy as spy

a = np.array([[3, 2, 1, 0], [2, 1, 0, 1], [1, 0, 1, 4], [1, 2, 1, 8]])
b = np.array([4, 2, 4, 2])

print('a:\n')
print(a)
print('\nb: ', b)

x = spy.linalg.solve_triangular(a, b, lower=True)

print('='*20)
print('x: ', x)
print('\ndot(a, x): ', np.dot(a, x))

