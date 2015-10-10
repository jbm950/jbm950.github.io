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
