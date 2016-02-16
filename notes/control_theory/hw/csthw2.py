import matplotlib.pyplot as plt
import numpy as np


def OLTF(s):
    output = 2.66*(s + 0.5)*(s + 100)/((s**2)*(s+10)**2*(s+2.9))
    return output

print(np.absolute(OLTF(1j)))


def prob4(kp, t):
    m = 20
    delta = m*kp*(np.exp(-0.7*t)*np.cos((11.4*kp - 0.7)*t) +
                  0.7/np.sqrt(11.4*kp-0.7)*np.exp(-0.7*t)*np.sin((11.4*kp -
                                                                  0.7)*t))
    return delta

t = np.arange(0, 7, 0.01)
kp = 25/20
y = [prob4(kp, i) for i in t]

plt.plot(t, y)
plt.show()
