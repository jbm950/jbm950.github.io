import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq

e = 1.602E-19
k = 1.381E-23

T = 273+32
iL = 0.035
io = 1.5E-10

partii = lambda Vm: np.exp((e*Vm)/(k*T)) * (1 + (e*Vm)/(k*T)) - 1 - iL/io
Vm = brentq(partii, 0, 1)
# print(Vm)

Voc = k*T/e*np.log(iL/io+1)
Ifunc = lambda V: iL - io*(np.exp((e*V)/(k*T)) -1)

V = np.arange(0, Voc, 0.0001)
I = [Ifunc(i) for i in V]
P = [I[i]*V[i] for i in range(len(V))]

plt.plot(V, I, V, P)
plt.title("Current and Power Response to Voltage")
plt.xlabel("Voltage (V)")
plt.ylabel("Current (A/cm^2), Power (W/cm^2)")
plt.legend(("Current (A/cm^2)", "Power (W/cm^2)"))
plt.show()
