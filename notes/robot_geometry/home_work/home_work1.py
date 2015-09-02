# This file will contain the computations required for the first homework

import numpy as np
import math as m
import rg_tools as rgt

print("\nProblem 2.3\n")

print("Part a.)\n")

T_C_A = np.matrix([[m.sqrt(2)/2, m.sqrt(2)/2, 0, 0],
                  [m.sqrt(2)/2, -m.sqrt(2)/2, 0, 0],
                  [0, 0, -1, 10],
                  [0, 0, 0, 1]])

T_A_B = np.matrix([[m.sqrt(3)/2, 0, 0.5, -10*m.sqrt(3)],
                  [0, -1, 0, 0],
                  [0.5, 0, -m.sqrt(3)/2, -10],
                  [0, 0, 0, 1]])

T_B_D = np.matrix([[1, 0, 0, 0],
                  [0, m.sqrt(3)/2, -0.5, -5*m.sqrt(3)],
                  [0, 0.5, m.sqrt(3)/2, -5],
                  [0, 0, 0, 1]])

T_C_D = T_C_A * T_A_B * T_B_D

print("T_C_A =\n", T_C_A, end="\n\n")
print("T_A_B =\n", T_A_B, end="\n\n")
print("T_B_D =\n", T_B_D, end="\n\n")

print("T_C_D =\n", T_C_D, end="\n\n")

print("Part b.)\n")

P1_D = np.matrix([[20], [-30], [5], [1]])

P1_B = T_B_D * P1_D
P1_A = T_A_B * P1_B
P1_C = T_C_A * P1_A

print("P1_D =\n", P1_D, end="\n\n")
print("P1_B =\n", P1_B, end="\n\n")
print("P1_A =\n", P1_A, end="\n\n")
print("P1_C =\n", P1_C, end="\n\n")

print("\nProblem 2.4\n")

vec = np.array([[2], [4], [7]])
theta = 60  # deg

T_A_C = np.matrix([[1, 0, 0, 3],
                   [0, 1, 0, 4],
                   [0, 0, 1, -2],
                   [0, 0, 0, 1]])

R_C_D = rgt.gen_vec_rotation_matrix(theta, vec)

T_C_D = np.matrix([[R_C_D[0, 0], R_C_D[0, 1], R_C_D[0, 2], 0],
                   [R_C_D[1, 0], R_C_D[1, 1], R_C_D[1, 2], 0],
                   [R_C_D[2, 0], R_C_D[2, 1], R_C_D[2, 2], 0],
                   [0, 0, 0, 1]])

T_D_B = np.matrix([[1, 0, 0, -3],
                   [0, 1, 0, -4],
                   [0, 0, 1, 2],
                   [0, 0, 0, 1]])

T_A_B = T_A_C * T_C_D * T_D_B

print("T_A_B = \n", T_A_B)

print("\nProblem 2.8\n")

T_A_D = np.matrix([[1, 0, 0, 10],
                   [0, 1, 0, 20],
                   [0, 0, 1, 10],
                   [0, 0, 0, 1]])
T_D_A = rgt.inv_trans_matrix(T_A_D)

alpha = np.radians(30)
T_D_E = np.matrix([[1, 0, 0, 0],
                   [0, m.cos(alpha), -m.sin(alpha), 0],
                   [0, m.sin(alpha), m.cos(alpha), 0],
                   [0, 0, 0, 1]])
T_E_D = rgt.inv_trans_matrix(T_D_E)

T_E_B = np.matrix([[1, 0, 0, -10],
                   [0, 1, 0, -20],
                   [0, 0, 1, -10],
                   [0, 0, 0, 1]])
T_B_E = rgt.inv_trans_matrix(T_E_B)

vec = np.array([[2], [4], [6]])
theta = 60  # deg
R_A_C = rgt.gen_vec_rotation_matrix(theta, vec)
T_A_C = np.matrix([[R_A_C[0, 0], R_A_C[0, 1], R_A_C[0, 2], 0],
                   [R_A_C[1, 0], R_A_C[1, 1], R_A_C[1, 2], 0],
                   [R_A_C[2, 0], R_A_C[2, 1], R_A_C[2, 2], 0],
                   [0, 0, 0, 1]])

T_B_C = T_B_E * T_E_D * T_D_A * T_A_C

print("T_B_C = \n", T_B_C)
