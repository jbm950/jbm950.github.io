# This file will be used during the first quiz for robot geometry

import numpy as np
import math as m
import rg_tools as rgt

# Useful functions to know for quizz
# np.cross(a, b) = cross product
#   - requires a and b to be row vectors
# np.linalg.norm(a) = magnitude
# a.transpose() = transpose of vector/matrix a

# Template for a vector
FP_1 = np.matrix([[0], [0], [0]])

# Template of the rotation matrix
R_1_2 = np.matrix([[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]])

# Template of the transformation matrix
T_1_2 = np.matrix([[0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 1]])

# Problem 1
print("\nProblem 1\n")

print("\nPart a\n")

AP_Borig = np.matrix([[2], [5], [1]])
thetaz = 50
thetax = 90

R_A_1 = rgt.rotation_about_z(thetaz)
R_1_B = rgt.rotation_about_x(thetax)

print("\n", R_A_1, "\n\n", R_1_B, "\n")

R_A_B = R_A_1 * R_1_B

print(R_A_B, "\n\n")

T_A_B = rgt.trans_matrix_form(R_A_B, AP_Borig)

print(T_A_B)

print("\nPart b\n")

[theta, mvec] = rgt.rev_gen_vec_rotation_matrix(R_A_B)

print("\n", mvec, "\n", theta)

# Problem 2
print("\nProblem 2\n")
