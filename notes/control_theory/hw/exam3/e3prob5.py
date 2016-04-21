from sympy import *

a1, a2, T1, T2 = symbols("a1 a2 T1 T2")
A = Matrix([[0, a2],
            [0,  0]])
B = Matrix([[0],
            [a1]])
C = Matrix([1, 0]).transpose()
T = Matrix([T1, T2])

################################################################################
#
# Part A
#
################################################################################

lam = symbols("lambda")
Delta = lam*eye(2) - (A - T*C)
Delta = Delta.det()
print("Part A\n------\n")
print("\nThe characteristic equation from state feedback is:")
pprint(collect(Delta.expand(), lam))

################################################################################
#
# Part B
#
################################################################################

Atilde = Matrix([[-T1, a2],
                 [-T2,  0]])
Btilde = Matrix([[T1,  0],
                 [T2, a1]])
Ctilde = eye(2)

s = symbols("s")
H = Ctilde*(s*eye(2) - Atilde).inv()*Btilde
H = H[:, 1]*Matrix([1, 0]).transpose() + H[:, 0]*Matrix([0, 1]).transpose()

print("\nPart B\n------")
print("\nThe M matrix can be given by:")
pprint(simplify(H))
