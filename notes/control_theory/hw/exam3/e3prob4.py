import numpy as np

################################################################################
#
# Part A
#
################################################################################

A = np.matrix([[-1,  0, -1],
               [ 1,  0,  0],
               [ 2, 10, -1]])
B = np.matrix([[6],
               [0],
               [10]])

AB = A*B
AAB = A*A*B

C = np.matrix([[B[0, 0], AB[0, 0], AAB[0, 0]],
               [B[1, 0], AB[1, 0], AAB[1, 0]],
               [B[2, 0], AB[2, 0], AAB[2, 0]]])

print("Part A\n------\n")
print("The controllability matrix is: ", end="")
print("\t[%.1f  %.1f %.1f]" % (C[0, 0], C[0, 1], C[0, 2]))
print("\t\t\t[%.1f  %.1f %.1f]" % (C[1, 0], C[1, 1], C[1, 2]))
print("\t\t\t[%.1f %.1f %.1f]" % (C[2, 0], C[2, 1], C[2, 2]))

rankC = np.linalg.matrix_rank(C)

print("\nThe rank of the controllability matrix, C, is: %d\n" % rankC)

################################################################################
#
# Part B
#
################################################################################

from sympy import *

lam = symbols("lambda")

Delta_C = (lam + 2)*(lam + 1 - I)*(lam + 1 + I)

print("Part B\n------\n")
print("The desired characteristic equation is:")
pprint(Delta_C.expand())

f1, f2, f3 = symbols("f1 f2 f3")
A = Matrix([[-1,  0, -1],
            [ 1,  0,  0],
            [ 2, 10, -1]])
B = Matrix([[6],
            [0],
            [10]])
F = Matrix([f1, f2, f3]).transpose()

Delta = lam*eye(3) - (A - B*F)
Delta = Delta.det()
print("\nThe characteristic equation from state feedback is:")
pprint(collect(Delta.expand(), lam))

E = np.matrix([[ 6,  0, 10],
               [-4,  6, 22],
               [ 0, -4, 60]])
g = np.matrix([[2],
               [3],
               [-6]])
Fsolved = np.linalg.solve(E, g)

print("\nThe gain matrix F = [%.3f, %.3f, %.3f]" % (Fsolved[0], Fsolved[1],
                                                    Fsolved[2]))
print("\nThis makes the characteristic polynomial the following:\n")

pprint(Delta.subs([(f1, Fsolved[0]), (f2, Fsolved[1]), (f3, Fsolved[2])]))


################################################################################
#
# Part C
#
################################################################################

C = Matrix([0, 0, 1]).transpose()
k = symbols("k")

Delta = lam*eye(3) - (A - B*k*C)
Delta = Delta.det()
print("\nPart C\n------\n")
print("The characteristic equation from state feedback is:")
pprint(collect(Delta.expand(), lam))
