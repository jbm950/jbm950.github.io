# This program will solve the problems for the third homework assignment that
# require programming
import math as m
import numpy as np


# Create the functions that will be required to answer the questions
def bisect(func, a, b, err):
    """This will perform the bisection root finding method to an input function
    in range [a, b] to a specified error
    Inputs:
        func - This is the function for which a root will be found
        a - Left endpoint of input interval
        b - Right endpoint of input interval
        err - Specified error tolerance"""

    fa = func(a)
    fb = func(b)

    # Test if the initial range includes a root
    if fa*fb > 0:
        print("Values\n\ta = %.4f\n\tf(a) = %.4f\n\tb = %.4f\n\tf(b) ="
              " %.4f\n\t" % (a, fa, b, fb))
        raise ValueError("There is no sign change in the function between the"
                         " end points a and b")
    elif fa == 0:
        return a
    elif fb == 0:
        return b

    nfinal = m.ceil(m.log((b - a)/err)/m.log(2))
    n = 0
    xnew = (a + b)/2

    while n < nfinal:
        fnew = func(xnew)
        if fnew == 0:
            return fnew
        elif fnew*fa < 0:
            b = xnew
            fb = fnew
        elif fnew*fb < 0:
            a = xnew
            fa = fnew
        else:
            # This code shouldn't run because bisection method shouldn't be able
            # to diverge
            print("Values\n\ta = %.4f\n\tf(a) = %.4f\n\tb = %.4f\n\tf(b) ="
                  " %.4f\n\tfnew = %.4f\n\tn = %d" % (a, fa, b, fb, fnew, n))
            raise ValueError("An error was encountered where there is no longer"
                             " a sign change")
        xnew = (a + b)/2
        fnew = func(xnew)
        n += 1

    return xnew


def newtons(func, fprime, x0, err):
    """This will use Newton's root finding method for an input function to a
    specified error tolerance
    Inputs:
        func - This is the function for which a root is being found
        fprime - This is the derivative of the function for which a root is
            being found
        x0 - This is the initial guess for the method
        err - This is the specified error tolerance"""

    n = 0
    xnew = x0 - func(x0)/fprime(x0)

    while np.absolute(xnew - x0) > err:
        x0 = xnew
        xnew = x0 - func(x0)/fprime(x0)
        n += 1

        if n > 1000:
            raise ValueError("Method appears to have diverged")

    return xnew


# Problem 2
# Define the error and the given functions
E = 1E-5
a = lambda x: m.exp(x) - 3*x**2
b = lambda x: x**3 - x**2 - x - 1
c = lambda x: m.exp(x) - 1/(0.1+x**2)
d = lambda x: x - 1 - 0.3 * m.cos(x)

# Calculate and present the roots and the value of the function at those roots
a_ans = bisect(a, -1, 5, E)
a_ans2 = bisect(a, 0.5, 1.5, E)
a_ans3 = bisect(a, -1, 0, E)
b_ans = bisect(b, -5, 5, E)
c_ans = bisect(c, -5, 5, E)
d_ans = bisect(d, -5, 5, E)
print("\nProblem 2")
print("\troot 1 of a: %.4f\tvalue of f(root) = %.7f" % (a_ans, a(a_ans)))
print("\troot 2 of a: %.4f\tvalue of f(root) = %.7f" % (a_ans2, a(a_ans2)))
print("\troot 3 of a: %.4f\tvalue of f(root) = %.7f" % (a_ans3, a(a_ans3)))
print("\troot of b: %.4f\tvalue of f(root) = %.7f" % (b_ans, b(b_ans)))
print("\troot of c: %.4f\tvalue of f(root) = %.7f" % (c_ans, c(c_ans)))
print("\troot of d: %.4f\tvalue of f(root) = %.7f" % (d_ans, d(d_ans)))


# Problem 4
aprime = lambda x: m.exp(x) - 6*x
bprime = lambda x: 3*x**2 - 2*x - 1
cprime = lambda x: m.exp(x) + 2*x/(0.1+x**2)**2
dprime = lambda x: 1 + 0.3 * m.sin(x)

a2_ans = newtons(a, aprime, 3.73, E)
a2_ans2 = newtons(a, aprime, 1, E)
a2_ans3 = newtons(a, aprime, -0.5, E)
b2_ans = newtons(b, bprime, 1.83, E)
c2_ans = newtons(c, cprime, 0.64, E)
d2_ans = newtons(d, dprime, 1, E)
print("\nProblem 4")
print("\troot 1 of a: %.4f\tvalue of f(root) = %.7f" % (a2_ans, a(a2_ans)))
print("\troot 2 of a: %.4f\tvalue of f(root) = %.7f" % (a2_ans2, a(a2_ans2)))
print("\troot 3 of a: %.4f\tvalue of f(root) = %.7f" % (a2_ans3, a(a2_ans3)))
print("\troot of b: %.4f\tvalue of f(root) = %.7f" % (b2_ans, b(b2_ans)))
print("\troot of c: %.4f\tvalue of f(root) = %.7f" % (c2_ans, c(c2_ans)))
print("\troot of d: %.4f\tvalue of f(root) = %.7f" % (d2_ans, d(d2_ans)))
print()

# Problem 39
p = lambda z: z**4 - 3*z**3 + 20*z**2 + 44*z + 54
pprime = lambda z: 4*z**3 - 9*z**2 + 40*z + 44

z0 = 2.5 + 4.5*1j
z1 = z0 - p(z0)/pprime(z0)
z2 = z1 - p(z1)/pprime(z1)
z3 = z2 - p(z2)/pprime(z2)
