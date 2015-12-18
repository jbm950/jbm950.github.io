# This file will contain code to interpolate functions using different methods

import math as m
import numpy as np


# Bell curve distribution
def bell_curve(x, mu, sigma):
    """This function will provide a base line test to compare the interpolation
    functions against.

    For a normal distribution mu = 0 and sigma = 1"""

    coef = 1/(sigma*m.sqrt(2 * m.pi))
    exponent = - (x - mu)**2 / (2 * sigma**2)

    return coef * m.exp(exponent)


# Interpolation using the formula of Lagrange
def lagrange_interpolation(x, xi, yi):
    """This function will perform the interpolation formula of lagrange"""
    output = 0
    for i in range(len(xi)):
        coef = 1
        for k in range(len(xi)):
            if k != i:
                coef *= (x - xi[k])/(xi[i] - xi[k])
            else:
                continue

        output += yi[i] * coef

    return output


if __name__ == "__main__":
    # Test the interpolation functions
    # r = real, i = interpolated
    x = np.arange(-1, 1.000001, 0.2)
    y = [bell_curve(a, 0, 1) for a in x]

    # Lagrange testing
    x1 = 0.25
    x1r = bell_curve(x1, 0, 1)
    x1i = lagrange_interpolation(x1, x, y)

    x2 = 0.75
    x2r = bell_curve(x2, 0, 1)
    x2i = lagrange_interpolation(x2, x, y)

    print("\nx1 = 0.25")
    print("\tReal value = %.4f" % x1r)
    print("\tInterpolated value = %.4f\n" % x1i)

    print("\nx2 = 0.75")
    print("\tReal value = %.4f" % x2r)
    print("\tInterpolated value = %.4f\n" % x2i)
