import matplotlib.pyplot as plt
import numpy as np

omega = 1.7
U = 9.5
R = 56
Cl = 1.16
CD = 0.1

r = np.arange(0, R, 0.01)
gam_v = [i*omega/U for i in r]
cpb = [x*(1+x**2)**(1/2)*(Cl-CD*x) for x in gam_v]

plt.plot(r, cpb)
plt.xlabel("Radial Distance, r (m)")
plt.ylabel("Blade Local Coefficient of Performance, c_p,B")
plt.title("Blade Local Coefficient of Performance vs. Radial Length")
plt.show()
