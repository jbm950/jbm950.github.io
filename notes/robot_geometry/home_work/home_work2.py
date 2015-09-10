# This file will contain the computations required for the second homework

import numpy as np
import math as m
import rg_tools as rgt

print("\nProblem 2.9\n")

theta1 = m.radians(35)
theta2 = m.radians(120)

R_A_C = np.matrix([[1, 0, 0], [0, m.cos(theta1), -m.sin(theta1)],
                   [0, m.sin(theta1), m.cos(theta1)]])
R_C_B = np.matrix([[m.cos(theta2), 0, m.sin(theta2)], [0, 1, 0],
                   [-m.sin(theta2), 0, m.cos(theta2)]])

R_A_B = R_A_C * R_C_B

[theta, mvec] = rgt.rev_gen_vec_rotation_matrix(R_A_B)

print("R_A_B =\n", R_A_B, end="\n\n")
print("Theta =\n", theta, end="\n\n")
print("mvec =\n", mvec, end="\n\n")
