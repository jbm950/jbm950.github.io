import numpy as np
import rg_tools as rgt

# Test values from homework 4's forward analysis
a67_F = np.matrix([[0.4082], [0.8165], [-.4082]])
S6_F = np.matrix([[-0.5774], [0.5774], [0.5774]])
Ptool_F = np.matrix([[80], [80], [18]])
Ptool_6 = np.matrix([[2], [3], [5]])

GE = rgt.GE_P60()
sol = GE.reverse_analysis(Ptool_6, Ptool_F, S6_F, a67_F)

solutions = ["A", "B", "C", "D", "E", "F", "G", "H"]

print("Solution\t\u03D51\t\t\u03F42\t\t\u03F43\t\t\u03F44\t\t\u03F45\t\t\u03F46")
for i in range(len(sol)):
    print(solutions[i], "\t\t", end="")
    for j in range(len(sol[0])):
        print("%.2f\t\t" % sol[i][j], end="")

    print()
