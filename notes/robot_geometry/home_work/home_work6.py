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
rgt.single_sub(alphas, 1, theta1, 1)

# ---
# Problem 6.5
# ---

print("\nProblem 6.5\n\n")
