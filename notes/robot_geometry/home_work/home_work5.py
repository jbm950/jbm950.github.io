import numpy as np
import rg_tools as rgt

Ptool_6 = np.matrix([[5], [3], [7]])
Ptool_F = np.matrix([[25], [23], [24]])
S6_F = np.matrix([[0.177], [0.884], [-0.433]])
a67_F = np.matrix([[-0.153], [0.459], [0.875]])


[S7, a71, S1, the7, alp71, gamma1] = rgt.close_the_loop(S6_F, a67_F, Ptool_F,
                                                        Ptool_6)

print("\nS7 =\n", S7, "\n")
print("\na71 =\n", a71, "\n")
print("\nS1 =\n", S1, "\n")
print("\nthe7 =\n", the7, "\n")
print("\nalp71 =\n", alp71, "\n")
print("\ngamma1 =\n", gamma1, "\n")
