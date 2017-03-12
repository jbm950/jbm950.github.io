import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simps
from scipy.special import iv

T1 = 750
Too = 300
L = 0.1
b = 0.05
h = 35
k = 25

z = np.arange(0, L, 0.0005)
temp = np.ones_like(z) * 750

for i in range(50):
    lam = (2*i+1) * np.pi / (2*L)

    num = np.array([h*(Too-T1)*np.sin(lam*j) for j in z])
    num = simps(num, z)
    denom = np.array([np.sin(lam*j)**2*(k*lam*iv(1, lam*b) + h*iv(0, lam*b)) for
                      j in z])
    denom = simps(denom, z)

    Cn = num/denom
    temp += np.array([Cn * np.sin(lam*j)*iv(0, 0) for j in z])

print("Temp\t\tz distance")
for i in range(len(temp)):
    print("%.1f K\t\t%.2f cm" % (temp[i], z[i] * 100))

plt.plot(z, temp)
plt.xlabel("z distance (m)")
plt.ylabel("Temperature (K)")
plt.title("Problem 5: Temp Variation along z for r = 0")
plt.show()
