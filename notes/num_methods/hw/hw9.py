import math as m
import matplotlib.pyplot as plt
import numpy as np

E1 = lambda x: np.sin(np.pi/2*x) - np.pi/2*x
E3 = lambda x: np.sin(np.pi/2*x) - np.pi/2*x + (np.pi*x/2)**3/m.factorial(3)
E5 = lambda x: np.sin(np.pi/2*x) - np.pi/2*x + (np.pi*x/2)**3/m.factorial(3) +\
               (np.pi*x/2)**5/m.factorial(5)

x = np.arange(-1, 1, 0.001)
y1 = [E1(x) for x in x]
y3 = [E3(x) for x in x]
y5 = [E5(x) for x in x]

plt.plot(x, y1, x, y3, "--", x, y5, "-.")
plt.xlabel("x")
plt.ylabel("Error")
plt.title("Error in Taylor Series Approximations to sin(pi/2*x)")
plt.legend(("E1(x)", "E3(x)", "E5(x)"))
plt.show()

f = lambda x: m.sqrt(1+x**2)
x = np.arange(0, 1, 0.001)
y = [f(x) for x in x]

plt.plot(x, y)
plt.show()
