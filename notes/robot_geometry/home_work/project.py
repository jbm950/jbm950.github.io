import numpy as np
import rg_tools as rgt

# Test values from homework 4's forward analysis
a67_F = np.matrix([[-0.59793388], [-0.75950066], [-0.25619098]])
S6_F = np.matrix([[0.74467828], [-0.64461587], [0.17298739]])
Ptool_F = np.matrix([[-2.71936583], [-7.53898355], [-144.38882145]])
Ptool_6 = np.matrix([[12], [8], [5]])

GE = rgt.GE_P60()
GE.reverse_analysis(Ptool_6, Ptool_F, S6_F, a67_F)
