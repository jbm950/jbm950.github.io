import numpy as np
import rg_tools as rgt

Ptool_6 = np.matrix([[5], [3], [7]])
Ptool_F = np.matrix([[25], [23], [24]])
S6_F = np.matrix([[0.177], [0.884], [-0.433]])
a67_F = np.matrix([[-0.153], [0.459], [0.875]])


A = rgt.T3_776()
A.close_the_loop(S6_F, a67_F, Ptool_F, Ptool_6)
