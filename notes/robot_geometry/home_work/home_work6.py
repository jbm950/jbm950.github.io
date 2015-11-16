import math as m
import numpy as np
import rg_tools as rgt

# ---
# Problem 6.2
# ---

print("\nProblem 6.2\n")

A = -0.1093
B = 0.6185
D = -0.5048

[check, theta1A, theta1B] = rgt.trig_solution(A, B, D)

print("theta1A:\n", theta1A, "\n")
print("theta1B:\n", theta1B, "\n")

# --
# Problem 6.3
# --

print("\nProblem 6.3\n\n")

alphas = [75, 110, 60, 80]
theta1 = 120
[X1, Y1, Z1] = rgt.single_sub(alphas, 1, theta1, 1)

print("X1:\n", X1, "\n")
print("Y1:\n", Y1, "\n")
print("Z1:\n", Z1, "\n")

# ---
# Problem 6.5
# ---

print("\nProblem 6.5\n\n")

# ---
# Testing against examples in the book
# ---

print("Testing functions against examples in the book (Section 6.7.2)\n")

alphas = [40, 70, 85, 70]
theta_4 = 75
[X_4, Y_4, Z_4] = rgt.single_sub(alphas, 4, theta_4, 0)

A = m.sin(m.radians(alphas[0])) * Y_4
B = m.sin(m.radians(alphas[0])) * X_4
D = m.cos(m.radians(alphas[0])) * Z_4 - m.cos(m.radians(alphas[1]))

print("Ac + Bs + D = 0")
print("A = %.4f" % A)
print("B = %.4f" % B)
print("D = %.4f" % D)

print()

[test, theta_1A, theta_1B] = rgt.trig_solution(A, B, D)

print("Theta 1A = %.2f" % theta_1A)
print("Theta 1B = %.2f" % theta_1B)

print()

[X_41A, Y_41A, Z_41A] = rgt.multi_sub_S(alphas, [[4, theta_4], [1, theta_1A]])
s2A = X_41A / m.sin(m.radians(alphas[1]))
c2A = Y_41A / m.sin(m.radians(alphas[1]))
theta_2A = m.degrees(np.arctan2(s2A, c2A))

[X_41B, Y_41B, Z_41B] = rgt.multi_sub_S(alphas, [[4, theta_4], [1, theta_1B]])
s2B = X_41B / m.sin(m.radians(alphas[1]))
c2B = Y_41B / m.sin(m.radians(alphas[1]))
theta_2B = m.degrees(np.arctan2(s2B, c2B))

print("Theta 2A = %.2f" % theta_2A)
print("Theta 2B = %.2f" % theta_2B)

print()

[X_14A, Y_14A, Z_14A] = rgt.multi_sub_S(alphas, [[1, theta_1A], [4, theta_4]])
s3A = X_14A / m.sin(m.radians(alphas[1]))
c3A = Y_14A / m.sin(m.radians(alphas[1]))
theta_3A = m.degrees(np.arctan2(s3A, c3A))

[X_14B, Y_14B, Z_14B] = rgt.multi_sub_S(alphas, [[1, theta_1B], [4, theta_4]])
s3B = X_14B / m.sin(m.radians(alphas[1]))
c3B = Y_14B / m.sin(m.radians(alphas[1]))
theta_3B = m.degrees(np.arctan2(s3B, c3B))

print("Theta 3A = %.2f" % theta_3A)
print("Theta 3B = %.2f" % theta_3B)

print()
