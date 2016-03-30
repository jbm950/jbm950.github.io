import numpy as np

# Initialize the requsite matrices and values
errtol = 1E-6
sizeN = 31
h = 1/sizeN
u1 = g = np.zeros((sizeN, sizeN))
x = y = np.arange(0, 1, h)
for j in range(len(y)):
    u1[0][j] = y[j]**2
    u1[j][-1] = x[j]**2
    g[j][j] = 4*j**2

u2 = np.copy(u1)
u3 = np.copy(u1)

print("\nThe errors ||x - x^(r)|| and ||x^(r+1) - x^(r)|| are not being"
      " displayed per iteration to save paper")


# Create functions to handle each part of the problem
def parta(h, u, x, errtol):
    """This function will solve the equation as requested by part a (jacobi
    method). Function assumes a square matrix.
    Inputs:
        h = distance between x and y values (delta x = delta y)
        u = starting matrix of solution values
        x = vector containing the x values (ranging from 0 to 1)
        errtol = specified tolerance for which to solve"""

    err = 100
    iteration = 1
    M = np.zeros((len(u)**2, len(u)**2))
    for it in np.arange(len(M) - 31*2) + 32:
        if it % 31 == 0:
            M[it - 1, it - 32] = 0
            M[it - 1, it - 2] = 0
            M[it - 1, it] = 0
            M[it - 1, it + 30] = 0
        else:
            M[it, it - 31] = 1/4
            M[it, it - 1] = 1/4
            M[it, it + 1] = 1/4
            M[it, it + 31] = 1/4
    c = []
    errbound = []
    while err > errtol:
        uprev = np.copy(u)
        errsum = 0
        for j in reversed(np.arange(len(u) - 2) + 1):
            for i in np.arange(len(u) - 2) + 1:
                u[j, i] = 1/4*(-h**2*g[j, i] + uprev[j+1, i] + uprev[j, i-1] +
                               uprev[j-1][i] + uprev[j, i+1])
                errsum += np.abs(u[j, i] - uprev[j, i])

        trueerrcurrentmat = u - uprev
        trueerrcurrentvec = np.zeros(len(M))
        it = 0
        for j in reversed(np.arange(len(u))):
            for i in np.arange(len(u)):
                trueerrcurrentvec[it] = trueerrcurrentmat[j, i]
                it += 1

        trueerrnextvec = M * trueerrcurrentvec

        errcurrent = np.linalg.norm(trueerrcurrentvec, ord=np.inf)
        errnext = np.linalg.norm(trueerrnextvec, ord=np.inf)
        c.append(errnext/errcurrent)
        errbound.append(c[-1]/(1/c[-1]) * errnext)

        err = 1/(len(u)-2)**2 * errsum
        # print(iteration)
        # print(err)
        iteration += 1

    print("\nPart a")
    print("It took: %d iterations" % iteration)
    print("The final error was: %.9f\n" % err)
    print("Estimate of constant c: %.4f" % c[-1])
    print("Estimate of error bound: %.9f\n" % errbound[-1])
    print("The answer matrix is:\n")
    print(u)


def partb(h, u, x, errtol):
    """This function will solve the equation as requested by part a (Gauss
    Seidel method). Function assumes a square matrix.
    Inputs:
        h = distance between x and y values (delta x = delta y)
        u = starting matrix of solution values
        x = vector containing the x values (ranging from 0 to 1)
        errtol = specified tolerance for which to solve"""

    err = 100
    iteration = 1
    M = np.zeros((len(u)**2, len(u)**2))
    for it in np.arange(len(M) - 31*2) + 32:
        if it % 31 == 0:
            M[it - 1, it - 32] = 0
            M[it - 1, it - 2] = 0
            M[it - 1, it] = 0
            M[it - 1, it + 30] = 0
        else:
            M[it, it - 31] = 1/4
            M[it, it - 1] = 1/4
            M[it, it + 1] = 1/4
            M[it, it + 31] = 1/4
    c = []
    errbound = []
    while err > errtol:
        uprev = np.copy(u)
        errsum = 0
        for j in reversed(np.arange(len(u) - 2) + 1):
            for i in np.arange(len(u) - 2) + 1:
                u[j, i] = 1/4*(-h**2*g[j, i] + u[j+1, i] + u[j, i-1] +
                               uprev[j-1, i] + uprev[j, i+1])
                errsum += np.abs(u[j, i] - uprev[j, i])

        trueerrcurrentmat = u - uprev
        trueerrcurrentvec = np.zeros(len(M))
        it = 0
        for j in reversed(np.arange(len(u))):
            for i in np.arange(len(u)):
                trueerrcurrentvec[it] = trueerrcurrentmat[j, i]
                it += 1

        trueerrnextvec = M * trueerrcurrentvec

        errcurrent = np.linalg.norm(trueerrcurrentvec, ord=np.inf)
        errnext = np.linalg.norm(trueerrnextvec, ord=np.inf)
        c.append(errnext/errcurrent)
        errbound.append(c[-1]/(1/c[-1]) * errnext)

        err = 1/(len(u)-2)**2 * errsum
        # print(iteration)
        # print(err)
        iteration += 1

    rate = 1 - np.pi**2 * h**2

    print("\nPart b")
    print("It took: %d iterations" % iteration)
    print("The final error was: %.9f\n" % err)
    print("Estimate of constant c: %.6f" % c[-1])
    print("Estimate of error bound: %.9f" % errbound[-1])
    print("Predicted iteration rate: %.6f\n" % rate)
    print("The answer matrix is:\n")
    print(u)


def partc(h, u, x, errtol):
    """This function will solve the equation as requested by part a (Gauss
    Seidel method). Function assumes a square matrix.
    Inputs:
        h = distance between x and y values (delta x = delta y)
        u = starting matrix of solution values
        x = vector containing the x values (ranging from 0 to 1)
        errtol = specified tolerance for which to solve"""

    err = 100
    iteration = 1
    Nele = u.shape[0] - 2
    ksi = 1 - 2*np.sin(np.pi/(2*Nele))**2
    omega = 2/(1+np.sqrt(1-ksi**2))
    while err > errtol:
        uprev = np.copy(u)
        errsum = 0
        for j in reversed(np.arange(len(u) - 2) + 1):
            for i in np.arange(len(u) - 2) + 1:
                u[j, i] = (omega * 1/4*(-h**2*g[j, i] + u[j+1, i] + u[j, i-1] +
                                        uprev[j-1, i] + uprev[j, i+1]) +
                           (1-omega) * uprev[j, i])
                errsum += np.abs(u[j, i] - uprev[j, i])

        err = 1/(len(u)-2)**2 * errsum
        # print(iteration)
        # print(err)
        iteration += 1

    print("\nPart c")
    print("It took: %d iterations" % iteration)
    print("The final error was: %.9f\n" % err)
    print("The answer matrix is:\n")
    print(u)


parta(h, u1, x, errtol)
partb(h, u2, x, errtol)
partc(h, u3, x, errtol)
