import matplotlib.pyplot as plt
import numpy as np


def func_a(x):
    return np.exp(-x**2)


def func_b(x):
    return 1/(1+x**2)


def trapezoidal(f, a, b, n):
    h = (b-a)/n
    fi = [f(i) for i in np.arange(a, b+h, h)]
    Ii = [0.5*(fi[i] + fi[i+1])*h for i in range(len(fi) - 1)]
    I = np.sum(Ii)

    return I


def simpsons(f, a, b, n):
    h = (b-a)/n
    fi = [f(i) for i in np.arange(a, b+h, h)]
    Ii = [h*(fi[2*i] + 4*fi[2*i+1] + fi[2*i+2])/3 for i in
          range(int((len(fi)-1)/2))]
    I = np.sum(Ii)

    return I


def tester(f, integrator, a, b):
    n = [2**n for n in np.arange(9)+1]
    I = [integrator(f, a, b, i) for i in n]
    R = [(I[i+1] - I[i])/(I[i+2] - I[i+1]) for i in range(len(I)-2)]

    return I, R


I_trap_a, R_trap_a = tester(func_a, trapezoidal, 0, 1)
I_trap_b, R_trap_b = tester(func_b, trapezoidal, -4, 4)
I_simp_a, R_simp_a = tester(func_a, simpsons, 0, 1)
I_simp_b, R_simp_b = tester(func_b, simpsons, -4, 4)

n = [i for i in range(9)]
n4R = [i for i in range(7)]
plt.plot(n, I_trap_a, n, I_simp_a, "--")
plt.figure()
plt.plot(n, I_trap_b, n, I_simp_b, "--")
plt.figure()
plt.plot(n4R, R_trap_a, n4R, R_simp_a, "--")
plt.figure()
plt.plot(n4R, R_trap_b, n4R, R_simp_b, "--")
plt.show()
