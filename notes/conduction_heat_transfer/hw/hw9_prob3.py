import matplotlib.pyplot as plt
import numpy as np
from scipy.special import erfc

L = 0.2  # m
T0 = 400  # K
k = 10  # W/mK
alpha = 2.2E-6  # m^2/s
x = 0.199  # m

t = np.arange(0.01, 4.01, 0.01)
iterations = 100
temp = np.zeros_like(t)

# Part ii
for j in range(len(t)):
    tot = 0

    for n in range(iterations):
        lam = (2*n+1) * np.pi / (2*L)
        tot += (-1)**n/lam*np.cos(lam*x)*np.exp(-alpha*lam**2*t[j])

    temp[j] = T0 - 2*T0/L * tot

# Part iii
temp2 = [T0*erfc((L-x)/np.sqrt(4*alpha*t[j])) for j in range(len(t))]

plt.plot(t, temp, t, temp2)
plt.xlabel("Time (s)")
plt.ylabel("Temperature (K)")
plt.title("Problem 3 Temp Variation at x = 0.199 m")
plt.legend(["Normal Method", "Small-Time Approximation"], loc=4)
plt.show()

t_temp = [i for i in t]
ts = [0, t_temp.index(1.0), t_temp.index(2.0), t_temp.index(3.0),
      t_temp.index(4.0)]

print("Time\t\tNormal Method\t\tSmall-Time Approximation")
for i in range(len(ts)):
    print("%.2f\t\t%.1f\t\t\t\t%.1f" % (t[ts[i]], temp[ts[i]], temp2[ts[i]]))
