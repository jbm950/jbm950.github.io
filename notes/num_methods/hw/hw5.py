import numpy as np


def func1(x, y):
    val = y + x**2 - x + 0.5
    return float(val)


def func2(x, y):
    val = x**2 - y - 5*x*y
    return float(val)


def jacob(x, y):
    a11 = 2*x - 1
    a12 = 1
    a21 = 2*x - 5*y
    a22 = -1 - 5*x
    return np.matrix([[a11, a12], [a21, a22]])


x = np.matrix([1.2, 1.2]).transpose()

for i in range(9):
    f1 = func1(x[0], x[1])
    f2 = func2(x[0], x[1])
    f = np.matrix([f1, f2]).transpose()
    J = jacob(float(x[0]), float(x[1]))
    delx = -1*np.linalg.solve(J, f)
    x[0] += delx[0]
    x[1] += delx[1]

    print("i = %d" % i, end="\n\t")
    print("f1 = %f" % f1, end="\n\t")
    print("f2 = %f" % f2, end="\n\t")
    print("J =\t[%f, %f]\n\t\t[%f, %f]" % (J[0, 0], J[0, 1], J[1, 0], J[1, 1]),
          end="\n\t")
    print("delx = %f" % delx[0], end="\n\t")
    print("dely = %f" % delx[1], end="\n\t")
    print("x = %f" % x[0], end="\n\t")
    print("y = %f" % x[1], end="\n\n")
