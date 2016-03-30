import matplotlib.pyplot as plt
import numpy as np

A = np.matrix([[6,   0,    0,   0],
               [1,   3,  0.5,   0],
               [0, 0.5,    2, 0.5],
               [0,   0, -1.5,   6]])
b = np.matrix([7.2, -6.6, 3.6, 3]).transpose()

S = np.linalg.solve(A, b)

S0 = 2*S[0, 0] - S[1, 0]
S5 = 3*S[-1, 0] - 2*S[-2, 0]

S = np.matrix([[S0],
               [S[0, 0]],
               [S[1, 0]],
               [S[2, 0]],
               [S[3, 0]],
               [S5]])

x = np.array([0, 1, 2, 2.5, 3, 4])
y = np.array([1.4, 0.6, 1.0, 0.65, 0.6, 1])
h = np.array([1, 1, 0.5, 0.5, 1])
a = np.zeros_like(h)
b = np.zeros_like(h)
c = np.zeros_like(h)
d = np.zeros_like(h)

for i in range(len(h)):
    a[i] = (S[i+1] - S[i])/(6*h[i])
    b[i] = S[i]/2
    c[i] = (y[i+1] - y[i])/h[i] - (2*h[i]*S[i] + h[i]*S[i+1])/6
    d[i] = y[i]


def cube_spline(x, data, a, b, c, d):
    if x < data[0]:
        raise IndexError("Interpolation only please")
    for i in np.array(range(len(data) - 1)) + 1:
        if x < data[i]:
            return d[i-1] + c[i-1]*(x-data[i-1]) + b[i-1]*(x-data[i-1])**2 + \
                   a[i-1]*(x-data[i-1])**3

    raise IndexError("Interpolation only please")

step = 0.01
xvals = np.arange(0, 4, step)
yvals = [cube_spline(i, x, a, b, c, d) for i in xvals]
cube_spline(2, x, a, b, c, d)

plt.plot(xvals, yvals)
plt.plot(x, y, 'ro')
plt.plot(x, y, '--')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Homework 8: Problem 1")
plt.legend(["Cubic Spline", "Data Points", "Linear Interpolation"])
plt.show()

A = np.matrix([[6, 16.5, 14], [16.5, 76.25, 48], [14, 48, 54]])
b = np.matrix([54, 243.5, 100]).transpose()
a = np.linalg.solve(A, b)
print(a)
