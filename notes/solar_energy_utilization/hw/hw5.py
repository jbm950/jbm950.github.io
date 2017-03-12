import matplotlib.pyplot as plt
import numpy as np
import random


def oneD_parabola(x, f):
    """Returns a y value for a given x value for a 2D parabolic surface"""
    return x**2/(4*f)


def twoD_parabola(x, y, f):
    """Returns a z value for a given x and y value for a 3D parabolic surface"""
    return (x**2 + y**2)/(4*f)


def step2(x1, y1, theta):
    """This function will take a point on the parabolic reflecting surface
    (x1,y1) and an acceptance angle (theta) and determine an vector for the
    incident radiation in the form of a new point a unit distance away from the
    given point ((x2-x1), (y2-y1))"""

    x2 = np.sin(theta) + x1
    y2 = np.sqrt(1 - (x2-x1)**2) + y1

    return x2, y2


def step3_twoD(x1, y1, f):
    """This function will find the tangent line to the parabolic surface at
    (x1,y1) in the form of a point defining a unit distance in the tangent
    direction from the input point ((x3-x1), (y3-y1))"""

    x3 = x1 + np.sqrt(4*f**2/(x1**2+4*f**2))
    if x1 < 0:
        y3 = y1 - np.sqrt(1-(x3-x1)**2)
    else:
        y3 = y1 + np.sqrt(1-(x3-x1)**2)

    return x3, y3


def step4(x1, y1, x3, y3):
    """This function will find the normal vector to the point on the parabolic
    surface ((x4-x1), (y4-y1))"""

    if x1 < 0:
        x4 = x1 + np.sqrt((y3-y1)**2 / ((x3-x1)**2 + (y3-y1)**2))
    else:
        x4 = x1 - np.sqrt((y3-y1)**2 / ((x3-x1)**2 + (y3-y1)**2))
    y4 = y1 + np.sqrt(1-(x4-x1)**2)

    return x4, y4


def step5(x1, y1, x2, y2, x4, y4):
    """This function will find the reflected vector from the incident vector and
    normal vector"""

    xr = x1-x2
    yr = y1-y2

    xn = x4-x1
    yn = y4-y1

    x5 = xr - 2 * (xn*xr+yn*yr) * xn + x1
    y5 = yr - 2 * (xn*xr+yn*yr) * yn + y1

    return x5, y5


def plane_intercept(x1, y1, x5, y5, y):
    return x5 + (x5-x1)/(y5-y1) * (y - y5)


def concentration_ratio_2D(n, y, D, f, theta):
    """
    Parameters:
        n: integer
            Number of incident rays
        y: numeric
            Distance from the bottom of the parameter where the concentration
            ratio is to be calculated
        D: numeric
            Diameter of the parabolic surface
        f: numeric
            Focal Distance
        theta: numeric
            Half acceptance angle of incomming radiation in degrees
    """

    incident = np.linspace(-D/2, D/2, n)
    deltaxs = np.linspace(-D/2, D/2, 500)
    deltax = deltaxs[1] - deltaxs[0]
    intercepted = np.zeros_like(deltaxs)

    for i in range(len(incident)):
        thetai = random.random() * theta * (-1)**random.randint(0, 1)
        thetai = np.radians(thetai)
        x1 = incident[i]
        y1 = oneD_parabola(x1, f)
        x2, y2 = step2(x1, y1, thetai)
        x3, y3 = step3_twoD(x1, y1, f)
        x4, y4 = step4(x1, y1, x3, y3)
        x5, y5 = step5(x1, y1, x2, y2, x4, y4)

        x = plane_intercept(x1, y1, x5, y5, y)

        for j in range(len(deltaxs)):
            if x < deltaxs[j]:
                intercepted[j-1] += 1
                break

    concentrations = np.zeros_like(intercepted)
    for i in range(len(intercepted)):
        concentrations[i] = (intercepted[i]/deltax)/(n/D)

    xs = [i + deltax/2 for i in deltaxs]

    return concentrations, xs

if __name__ == "__main__":
    con1, xs = concentration_ratio_2D(1000, 2, 6, 2, 0.25)
    con2, xs = concentration_ratio_2D(1000, 2, 6, 2, 1)
    con3, xs = concentration_ratio_2D(1000, 2, 6, 2, 5)
    con4, xs = concentration_ratio_2D(1000, 2, 6, 2, 10)

    plt.figure("Problem 1")

    plt.title("Concentration Ratios")
    plt.subplot(2, 2, 1)
    plt.title("theta = 0.25 deg")
    plt.ylabel("Concentration Ratio")
    plt.plot(xs, con1)

    plt.subplot(2, 2, 2)
    plt.title("theta = 1 deg")
    plt.ylabel("Concentration Ratio")
    plt.plot(xs, con2)

    plt.subplot(2, 2, 3)
    plt.title("theta = 5 deg")
    plt.ylabel("Concentration Ratio")
    plt.plot(xs, con3)

    plt.subplot(2, 2, 4)
    plt.title("theta = 10 deg")
    plt.ylabel("Concentration Ratio")
    plt.plot(xs, con4)

    plt.show()

    con5, xs = concentration_ratio_2D(100000, 0.75*2, 6, 2, 1)
    con6, xs = concentration_ratio_2D(100000, 1.25*2, 6, 2, 1)

    plt.figure("Problem 2")

    plt.title("Concentration Ratios")
    plt.subplot(2, 1, 1)
    plt.title("Distance 0.75f")
    plt.ylabel("Concentration Ratio")
    plt.plot(xs, con5)

    plt.subplot(2, 1, 2)
    plt.title("Distance 1.25f")
    plt.ylabel("Concentration Ratio")
    plt.plot(xs, con6)

    plt.show()
