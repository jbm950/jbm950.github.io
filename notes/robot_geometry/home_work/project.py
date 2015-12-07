import numpy as np
import rg_tools as rgt

# Test values from homework 4's forward analysis
a67_F = np.matrix([[0.4082], [0.8165], [-.4082]])
S6_F = np.matrix([[-0.5774], [0.5774], [0.5774]])
Ptool_F = np.matrix([[80], [80], [18]])
Ptool_6 = np.matrix([[2], [3], [5]])
S6 = 15.24

GE = rgt.GE_P60()
sol = GE.reverse_analysis(Ptool_6, Ptool_F, S6_F, a67_F, S6)

print("_" * 50)
print("\nInputs:\n")

print("S6 = %.2f cm\n" % S6)

invectors = [["a67_F", a67_F], ["S6_F", S6_F], ["Ptool_F", Ptool_F],
             ["Ptool_6", Ptool_6]]

for i in range(int(len(invectors)/2)):
    print("\t\t[%.4f]\t\t\t  [%.4f]" % (invectors[i][1][0], invectors[i+2][1][0]))
    print("%s =\t[%.4f]\t%s = [%.4f]" % (invectors[i][0], invectors[i][1][1],
                                         invectors[i+2][0],
                                         invectors[i+2][1][1]))
    print("\t\t[%.4f]\t\t\t  [%.4f]\n" % (invectors[i][1][2], invectors[i+2][1][2]))

solutions = ["A", "B", "C", "D", "E", "F", "G", "H"]

print("_" * 50, "\nReverse Analysis\n")
print("Solution\t\u03D51\t\t\t\u03F42\t\t\t\u03F43\t\t\t\u03F44\t\t\t\u03F45\t\t\t\u03F46")
for i in range(len(sol)):
    print(solutions[i], "\t\t\t", end="")
    for j in range(len(sol[0])):
        print("%.2f\t\t" % sol[i][j], end="")

    print()

print("_" * 50, "\nForward Analysis Check\n")

Ptool6 = [int(x) for x in Ptool_6]
for i in range(len(solutions)):
    print("_" * 25)
    print("Case %s:\n" % solutions[i])
    [fa_a67_F, fa_S6_F, fa_Ptool_F] = GE.forward_analysis(GE.joint_offsets[1:6],
                                                          sol[i], Ptool6)

    print("\t\t[%.4f]\t\t\t[%.4f]\t\t\t  [%.4f]" % (fa_a67_F[0], fa_S6_F[0],
                                              fa_Ptool_F[0]))
    print("a67_F =\t[%.4f]\tS6_F =\t[%.4f]\tPtool_F = [%.4f]" % (fa_a67_F[1],
                                                                 fa_S6_F[1],
                                                                 fa_Ptool_F[1]))
    print("\t\t[%.4f]\t\t\t[%.4f]\t\t\t  [%.4f]\n" % (fa_a67_F[2], fa_S6_F[2],
                                                fa_Ptool_F[2]))
