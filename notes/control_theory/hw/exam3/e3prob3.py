import numpy as np

################################################################################
#
# Part A
#
################################################################################

A = np.matrix([[   0,    1],
               [-0.4, -1.3]])
C = np.matrix([0.8, 1])

CA = C*A

O = np.matrix([[ C[0, 0],  C[0, 1]],
               [CA[0, 0], CA[0, 1]]])

print("Part A\n------\n")
print("The observability matrix is: ", end="")
print("\t[%.1f   %.1f]\n\t\t\t\t\t\t\t\t[%.1f %.1f]" % (O[0, 0], O[0, 1],
                                                        O[1, 0], O[1, 1]))

rankO = np.linalg.matrix_rank(O)

print("\nThe rank of the observability matrix, O, is: %d" % rankO)

################################################################################
#
# Part B
#
################################################################################

A = np.matrix([[-1.3, 1],
               [-0.4, 0]])
B = np.matrix([[  1],
               [0.8]])

AB = A*B

C = np.matrix([[B[0, 0], AB[0, 0]],
               [B[1, 0], AB[1, 0]]])

print("\nPart B\n------\n")
print("The controllability matrix is: ", end="")
print("\t[%.1f  %.1f]\n\t\t\t\t\t\t\t\t[%.1f  %.1f]" % (C[0, 0], C[0, 1],
                                                        C[1, 0], C[1, 1]))

rankC = np.linalg.matrix_rank(C)

print("\nThe rank of the controllability matrix, C, is: %d" % rankC)
