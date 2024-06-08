try:
    from ulab import numpy
    from ulab import scipy
except ImportError:
    import numpy
    import scipy.special

x = numpy.array([1, 2, 3])
scipy.special.erf(x)

