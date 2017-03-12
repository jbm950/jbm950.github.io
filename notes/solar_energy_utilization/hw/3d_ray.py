from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import random


def threeD_parabola(x, y, f):
    """Returns a z value for a given x and y value for a 3D parabolic surface"""
    return (x**2 + y**2)/(4*f)


def step2(x1, y1, z1, theta, phi):

    phis = np.radians(phi)
    if phi < 90 or phi > 270:
        x2 = x1 + np.sqrt((1-np.cos(theta)**2)/(1+np.tan(phis)**2))
    else:
        x2 = x1 - np.sqrt((1-np.cos(theta)**2)/(1+np.tan(phis)**2))

    if phi < 180:
        y2 = y1 + np.abs((x2-x1)*np.tan(phis))
    else:
        y2 = y1 - np.abs((x2-x1)*np.tan(phis))

    z2 = z1 + np.cos(theta)

    return x2, y2, z2


def step4(x1, y1, f):
    x4 = -x1/2/f
    y4 = -y1/2/f
    z4 = 1

    return x4, y4, z4


def step5(x1, y1, z1, x2, y2, z2, x4, y4, z4):
    xr = x1-x2
    yr = y1-y2
    zr = z1-z2

    xn = x4-x1
    yn = y4-y1
    zn = z4-z1

    x5 = xr - 2 * (xn*xr+yn*yr+zr*zn) * xn + x1
    y5 = yr - 2 * (xn*xr+yn*yr+zr*zn) * yn + y1
    z5 = zr - 2 * (xn*xr+yn*yr+zr*zn) * zn + z1

    return x5, y5, z5


def concentration_ratio_3D(n, D, f, theta):
    """n = number of rows (equal number of rows and columns)"""

    # Create the x,y pairs to do rays for
    xtemp = np.linspace(-D/2, D/2, n)
    ytemp = np.linspace(-D/2, D/2, n)
    x1 = []
    y1 = []
    for i in range(n):
        for j in range(n):
            if xtemp[i]**2 + ytemp[j]**2 < (D/2)**2:
                x1 += [xtemp[i]]
                y1 += [ytemp[j]]

    # Step 1 find the z values that correspond to each x and y value
    z1 = np.zeros_like(x1)
    for i in range(len(x1)):
        z1[i] = threeD_parabola(x1[i], y1[i], f)

    # Step 2 determine where the incident ray is coming from
    x2 = np.zeros_like(z1)
    y2 = np.zeros_like(z1)
    z2 = np.zeros_like(z1)
    for i in range(len(z1)):
        thetas = theta * random.random()
        thetas = np.radians(thetas)
        phi = 360 * random.random()
        x2[i], y2[i], z2[i] = step2(x1[i], y1[i], z1[i], thetas, phi)

    # Step 4 to get vector normal to the tangent plane
    x4 = np.zeros_like(z1)
    y4 = np.zeros_like(z1)
    z4 = np.zeros_like(z1)
    for i in range(len(z1)):
        x4[i], y4[i], z4[i] = step4(x1[i], y1[i], f)

    # Step 5
    x5 = np.zeros_like(z1)
    y5 = np.zeros_like(z1)
    z5 = np.zeros_like(z1)
    for i in range(len(z1)):
        x5[i], y5[i], z5[i] = step5(x1[i], y1[i], z1[i], x2[i], y2[i], z2[i],
                                    x4[i], y4[i], z4[i])

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    for i in range(len(x1)):
        ax.plot([x1[i], x2[i]], [y1[i], y2[i]], [z1[i], 0.35*z2[i]], "g")
        # ax.plot([x1[i], x5[i]], [y1[i], y5[i]], [z1[i], z5[i]], "b")

    plt.title("theta_s = %.2f" % theta)
    plt.legend(["incident", "reflected"])
    plt.show()


concentration_ratio_3D(15, 6, 4, 0.25)
concentration_ratio_3D(15, 6, 4, 10)
