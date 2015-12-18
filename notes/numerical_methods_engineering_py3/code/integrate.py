# This file will contain different numerical integration techniques

import math as m
import numpy as np


# Bell curve distribution as a function to test the integration methods
def bell_curve(x, mu, sigma):
    """This function will provide a base line test to compare the interpolation
    functions against.

    For a normal distribution mu = 0 and sigma = 1"""

    coef = 1/(sigma*m.sqrt(2 * m.pi))
    exponent = - (x - mu)**2 / (2 * sigma**2)

    return coef * m.exp(exponent)


# This function will use simpsons rule to integrate a function
def simpsons(func, a, b, subintervals, args):
    """This function will implement simpsons rule for determining an integral.
    The args input are the extra inputs that will be needed to run the generic
    func input"""

    # First split range [a,b] into subintervals
    x = np.linspace(a, b, subintervals)
    h = (x[1] - x[0])/2

    # For each subinterval find the approximate integrated value and add it to a
    # total sum
    total = 0
    for i in range(len(x) - 1):
        f0 = func(x[i], *args)
        f1 = func(x[i] + h, *args)
        f2 = func(x[i + 1], *args)
        total += h/3*(f0 + 4*f1 + f2)

    return total


# This function will perform 3 point gaussian quadrature for a user specified
# number of subintervals
def three_gauss(func, a, b, subintervals, args):
    """3 point gaussian quadrature will be used on the specified number of
    subintervals. The args input are the extra inputs that will be needed to run
    the generic func input"""
    # First split the range [a, b] into subintervals
    x = np.linspace(a, b, subintervals)

    # Set up 3 point gauss quadrature weights and points
    c1 = 5/9
    c2 = 8/9
    c3 = 5/9

    x1 = - 0.7745966692
    x2 = 0
    x3 = 0.7745966692

    # Perform gaussian quadrature to approximate the integral
    total = 0
    for i in range(len(x) - 1):
        m = (x[i+1] - x[i])/2
        f1 = func((x[i+1] - x[i])/2 * x1 + (x[i+1] + x[i])/2, *args)
        f2 = func((x[i+1] - x[i])/2 * x2 + (x[i+1] + x[i])/2, *args)
        f3 = func((x[i+1] - x[i])/2 * x3 + (x[i+1] + x[i])/2, *args)
        total += m * (c1 * f1 + c2 * f2 + c3 * f3)

    return total


# Testing function
def tester1(method):
    """This function will test a given integration method with the bell curve
    function for 3 ranges and multiple intervals
    Inputs:
        method - This is the integration method that is being tested
            method(func, a, b, subintervals, args) format"""

    print("\tNormal Distribution: -1 to 1 (1 standard deviation)")
    print("\t\t", method(bell_curve, -1, 1, 2, [0, 1]), "\t(2 Subintervals)")
    print("\t\t", method(bell_curve, -1, 1, 6, [0, 1]), "\t(6 Subintervals)")
    print("\t\t", method(bell_curve, -1, 1, 15, [0, 1]),
          "\t(15 Subintervals)")
    print("\t\t", method(bell_curve, -1, 1, 75, [0, 1]),
          "\t(75 Subintervals)")
    print("\t\t", method(bell_curve, -1, 1, 500, [0, 1]),
          "\t(500 Subintervals)")
    print("\n")

    print("\tNormal Distribution: -2 to 2 (2 standard deviations)")
    print("\t\t", method(bell_curve, -2, 2, 2, [0, 1]),
          "   \t(2 Subintervals)")
    print("\t\t", method(bell_curve, -2, 2, 6, [0, 1]),
          "\t(6 Subintervals)")
    print("\t\t", method(bell_curve, -2, 2, 15, [0, 1]),
          "\t(15 Subintervals)")
    print("\t\t", method(bell_curve, -2, 2, 75, [0, 1]),
          "\t(75 Subintervals)")
    print("\n")

    print("\tNormal Distribution: -3 to 3 (3 standard deviations)")
    print("\t\t", method(bell_curve, -3, 3, 2, [0, 1]),
          "\t\t(2 Subintervals)")
    print("\t\t", method(bell_curve, -3, 3, 6, [0, 1]),
          "\t(6 Subintervals)")
    print("\t\t", method(bell_curve, -3, 3, 15, [0, 1]),
          "\t(15 Subintervals)")
    print("\t\t", method(bell_curve, -3, 3, 75, [0, 1]),
          "\t(75 Subintervals)")
    print("\n")


if __name__ == "__main__":
    print("\nSimpson's rule\n")
    tester1(simpsons)

    print("\n3-pt Gaussian Quadrature\n")
    tester1(three_gauss)
