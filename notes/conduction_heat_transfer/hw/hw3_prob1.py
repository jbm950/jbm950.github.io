import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simps

L = 0.1
alpha = 8.418E-5
x = np.linspace(0, L, 2000)


def initial_temp(x):
    return 200 + 3000*x

times = np.linspace(0, 80, 200)
temp = np.zeros_like(times)
for j in range(len(times)):
    tot = 0

    for i in range(30):
        lam = np.pi * i / L

        num = np.array([initial_temp(i)*np.cos(lam*i) for i in x])
        num = simps(num, x)
        denom = np.array([np.cos(lam*i)**2 for i in x])
        denom = simps(denom, x)

        Cn = num/denom
        tot += Cn*np.cos(lam*L)*np.exp(-alpha*lam**2*times[j])

    temp[j] = tot

plt.plot(times, temp)
plt.xlabel("Time (s)")
plt.ylabel("Temperature (deg C)")
plt.title("Problem 1 Temp Variation at x = L")
plt.show()
