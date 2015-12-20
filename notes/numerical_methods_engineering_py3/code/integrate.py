# This file will contain different numerical integration techniques

import math as m
import multiprocessing as mp
import numpy as np
import timer


# Bell curve distribution as a function to test the integration methods
def bell_curve(x, mu, sigma):
    """This function will provide a base line test to compare the interpolation
    functions against.

    For a normal distribution mu = 0 and sigma = 1"""

    coef = 1/(sigma*m.sqrt(2 * m.pi))
    exponent = - (x - mu)**2 / (2 * sigma**2)

    return coef * m.exp(exponent)


# Bell curve distribution as a function to test the integration methods
def bell_curve_one(inp):
    """This function will provide a base line test to compare the interpolation
    functions against.

    For a normal distribution mu = 0 and sigma = 1"""

    [x, mu, sigma] = inp

    coef = 1/(sigma*m.sqrt(2 * m.pi))
    exponent = - (x - mu)**2 / (2 * sigma**2)

    return coef * m.exp(exponent)


# +----------------------------------------------------------------------------+
# Newton-Cotes Fomula                                                          |
# +----------------------------------------------------------------------------+

# Simpsons Formula
# ----------------

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


# This function will use simpsons rule to integrate a function to a specified
# error tolerance using multiprocessing for the subintervals
def simpsons_err(func, a, b, err, args):
    """This function will implement simpsons rule for determining an integral.
    The args input are the extra inputs that will be needed to run the generic
    func input"""

    # First split range [a,b] into subintervals
    subintervals = 2
    x = np.linspace(a, b, subintervals)

    # Function to calculate the value for a subinterval
    def subinter(rans, total, x, func):
        """ran - [a, b] range of the sub interval"""
        h = (rans[0][1] - rans[0][0])/2
        args = [0, 1]
        subtotal = 0
        for i in rans:
            f0 = func(i[0], *args)
            f1 = func(i[0] + h, *args)
            f2 = func(i[1], *args)
            subtotal += h/3*(f0 + 4*f1 + f2)

        total[x] = subtotal

    # For each subinterval find the approximate integrated value and add it to a
    # total sum
    prev_total = 0
    total = [0]
    ranges = [[x[i], x[i+1]] for i in range(len(x) - 1)]
    subinter([ranges[0]], total, 0, func)
    total = sum(total)
    cores = mp.cpu_count()

    while m.fabs(prev_total - total) > err:
        prev_total = total
        subintervals += 1
        x = np.linspace(a, b, subintervals)

        ranges = [[x[i], x[i+1]] for i in range(len(x) - 1)]
        workers = []
        if len(ranges) > cores:
            total = mp.Array('f', range(cores))
            dist = m.floor(len(ranges)/cores)
            for i in range(cores):
                if i == cores - 1:
                    workers += [mp.Process(target=subinter,
                                           args=(ranges[dist*i:len(ranges)],
                                                 total, i, func))]
                elif i == 0:
                    workers += [mp.Process(target=subinter,
                                           args=(ranges[dist*i:dist*i+dist],
                                                 total, i, func))]
                else:
                    workers += [mp.Process(target=subinter,
                                           args=(ranges[dist*i:dist*i+dist],
                                                 total, i, func))]
        else:
            total = mp.Array('f', range(len(ranges)))
            for i in range(len(ranges)):
                workers += [mp.Process(target=subinter,
                                       args=([ranges[i]], total, i, func))]

        for w in workers:
            w.start()

        for w in workers:
            w.join()

        total = sum(total)

    # print("Final result for error tolerance of "
    #       "%f took %d subintervals" % (err, subintervals))

    return total


# This function will use simpsons rule to integrate a function to a specified
# error tolerance
def simpsons_err2(func, a, b, err, args):
    """This function will implement simpsons rule for determining an integral.
    The args input are the extra inputs that will be needed to run the generic
    func input"""

    # First split range [a,b] into subintervals
    subintervals = 2
    x = np.linspace(a, b, subintervals)
    h = (x[1] - x[0])/2

    # For each subinterval find the approximate integrated value and add it to a
    # total sum
    prev_total = 50
    total = 0
    for i in range(len(x) - 1):
        f0 = func(x[i], *args)
        f1 = func(x[i] + h, *args)
        f2 = func(x[i + 1], *args)
        total += h/3*(f0 + 4*f1 + f2)

    while m.fabs(prev_total - total) > err:
        prev_total = total
        total = 0
        subintervals += 1
        x = np.linspace(a, b, subintervals)
        h = (x[1] - x[0])/2

        for i in range(len(x) - 1):
            f0 = func(x[i], *args)
            f1 = func(x[i] + h, *args)
            f2 = func(x[i + 1], *args)
            total += h/3*(f0 + 4*f1 + f2)

    # print("Final result for error tolerance of "
    #       "%f took %d subintervals" % (err, subintervals))

    return total


# +----------------------------------------------------------------------------+
# Gauss Quadrature                                                             |
# +----------------------------------------------------------------------------+

# Three Point Gauss Quadrature
# ----------------------------

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


# This function will perform 3 point gaussian quadrature for a user specified
# error tolerance
def three_gauss_err(func, a, b, err, args):
    """3 point gaussian quadrature will be used on the specified number of
    subintervals. The args input are the extra inputs that will be needed to run
    the generic func input"""
    # First split the range [a, b] into subintervals
    subintervals = 2
    x = np.linspace(a, b, subintervals)

    # Set up 3 point gauss quadrature weights and points
    c1 = 5/9
    c2 = 8/9
    c3 = 5/9

    x1 = - 0.7745966692
    x2 = 0
    x3 = 0.7745966692

    # Perform gaussian quadrature to approximate the integral
    prev_total = 0
    total = 0
    for i in range(len(x) - 1):
        m1 = (x[i+1] - x[i])/2
        f1 = func((x[i+1] - x[i])/2 * x1 + (x[i+1] + x[i])/2, *args)
        f2 = func((x[i+1] - x[i])/2 * x2 + (x[i+1] + x[i])/2, *args)
        f3 = func((x[i+1] - x[i])/2 * x3 + (x[i+1] + x[i])/2, *args)
        total += m1 * (c1 * f1 + c2 * f2 + c3 * f3)

    while m.fabs(total - prev_total) > err:
        prev_total = total
        subintervals += 1
        x = np.linspace(a, b, subintervals)

        total = 0
        for i in range(len(x) - 1):
            m1 = (x[i+1] - x[i])/2
            f1 = func((x[i+1] - x[i])/2 * x1 + (x[i+1] + x[i])/2, *args)
            f2 = func((x[i+1] - x[i])/2 * x2 + (x[i+1] + x[i])/2, *args)
            f3 = func((x[i+1] - x[i])/2 * x3 + (x[i+1] + x[i])/2, *args)
            total += m1 * (c1 * f1 + c2 * f2 + c3 * f3)

    # print("Final result for error tolerance of "
    #       "%f took %d subintervals" % (err, subintervals))

    return total


# +----------------------------------------------------------------------------+
# Testing Functions                                                            |
# +----------------------------------------------------------------------------+

# Testing function for ranges (-1, 1), (-2, 2), (-3, 3) of the bell curve for
# the functions with user specified subintervals
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
    # print("\nSimpson's rule\n")
    # tester1(simpsons)

    # print("\n3-pt Gaussian Quadrature\n")
    # tester1(three_gauss)

    # timer.timer(three_gauss, [bell_curve, -1, 1, 100, [0, 1]], 500)
    # timer.timer(simpsons, [bell_curve, -1, 1, 500, [0, 1]], 500)
    print(three_gauss_err(bell_curve, -1, 1, 1E-10, [0, 1]))
    print(simpsons_err(bell_curve, -3, 3, 1E-10, [0, 1]))
    print(simpsons_err2(bell_curve, -3, 3, 1E-10, [0, 1]))

    print("\n3-pt Gaussian Quadrature\n")
    timer.timer(three_gauss_err, [bell_curve, -1, 1, 1E-9, [0, 1]], 50)

    print("\nSimpson's rule\n")
    print("\tParallel Processing\n\t\t", end="")
    timer.timer(simpsons_err, [bell_curve, -1, 1, 1E-9, [0, 1]], 50)
    print("\tOriginal\n\t\t", end="")
    timer.timer(simpsons_err2, [bell_curve, -1, 1, 1E-9, [0, 1]], 50)
