# This file will contain different approaches to solving systems of equations
# of the form Ax = b

import numpy as np
import timer


# +----------------------------------------------------------------------------+
# Gauss Elimination                                                            |
# +----------------------------------------------------------------------------+

def gauss_elim(A, b):
    """This function will solve a system of equations using the gaussian
    elimination method
    Inputs:
        A - coefficient matrix of Ax = b
        b - constant matrix of Ax = b"""

    # Forward Elimination Phase
    for i in range(len(b) - 1):
        for j in range(i, len(b) - 1):
            A[j+1, i:] = A[j+1, i:] - A[j+1, i] / A[i, i] * A[i, i:]
            b[j+1] = b[j+1] - A[j+1, i] / A[i, i] * b[i]

    # Back Substitution Phase
    x = np.zeros(len(b))
    x[-1] = b[-1] / A[-1, -1]
    for i in range(len(b) - 2, -1, -1):
        x[i] = (b[i] - np.dot(np.array(A[i, i+1:])[0], x[i+1:])) / A[i, i]

    return x


if __name__ == "__main__":
    A = np.matrix([[5, 2, 3, 5, 6],
                   [3, 4, 1, 9, 3],
                   [4, 2, 6, 8, 1],
                   [5, 2, 8, 1, 9],
                   [4, 1, 3, 4, 6]])
    b = np.matrix([3, 5, 2, 6, 3]).transpose()

    print("\n")
    print("Gaussian Elimination\n\t", end="")
    print(gauss_elim(A, b), end="\n\t")
    timer.timer(gauss_elim, [A, b], 500)
    print("\n")

    print("Numpy's linalg.solve() Method", end="\n\t")
    print(np.linalg.solve(A, b).transpose(), end="\n\t")
    timer.timer(np.linalg.solve, [A, b], 50000)
    print("\n")
