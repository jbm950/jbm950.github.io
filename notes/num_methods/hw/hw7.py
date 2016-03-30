import functools
import math as m
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return 1/(1+x**2)


def p12(x):
    delf0 = [0.03846, 0.01599, 0.01214, 0.01505, 0.02914, 0.05437, -0.3809,
             0.1627, 3.1939, -14.8763, 43.2103, -99.8783, 199.7566]
    h = 10/12
    s = (x + 5)/h
    sumation = 0
    for i in range(13):
        if i == 0:
            sumation += delf0[i]
        else:
            ss = [s - j for j in range(i)]
            ssum = functools.reduce(lambda x, y: x*y, ss)
            sumation += ssum*delf0[i]/m.factorial(i)

    return sumation

x = np.arange(-5, 5, 0.01)
ya = [p12(i) for i in x]
yt = [f(i) for i in x]
err = [yt[i] - ya[i] for i in range(len(yt))]

plt.plot(x, err)
plt.ylabel("E12(x)")
plt.xlabel("x")
plt.title("Error for 12 point polynomial interpolation of f(x)")
plt.show()
