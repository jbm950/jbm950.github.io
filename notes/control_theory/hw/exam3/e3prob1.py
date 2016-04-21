import numpy as np

A = np.matrix([[0, 1,  0],
               [0, 0,  1],
               [0, 0, -1]])

eigA = np.linalg.eig(A)[0]
print("The eigen values of matrix A are %.2f, %.2f, %.2f" % (eigA[0], eigA[1],
                                                             eigA[2]))
