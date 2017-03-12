import datetime
import math
import numpy as np


def is_near(value, test, tol):
    "Is Value near Test +- tol?"
    if value > test - tol and value < test + tol:
        return True
    else:
        return False


def equation_of_time(date):
    """This is the term E in the solar time -> local time conversion"""
    n = abs(datetime.date(date.year, 1, 1) - date).days + 1
    B = np.radians((n-1)*360/365)
    E = 229.2 * (0.000075 + 0.001868*np.cos(B) - 0.032077*np.sin(B) -
                 0.014615*np.cos(2*B) - 0.04089*np.sin(2*B))

    return E


def hour_angle(solartime):
    noon = datetime.time(12, 0, 0)

    # Find the time difference from solar noon
    min_diff = solartime.minute - noon.minute
    if min_diff < 0:
        min_diff = (60 + min_diff)/60
        carryover = 1
    else:
        min_diff = min_diff/60
        carryover = 0
    hour_diff = solartime.hour - noon.hour - carryover + min_diff

    omega = 15 * hour_diff

    return omega


def incidence_angle(theta_z, beta, gamma_s, gamma):
    # Convert all degrees to radians
    theta_z = np.radians(theta_z)
    beta = np.radians(beta)
    gamma_s = np.radians(gamma_s)
    gamma = np.radians(gamma)

    inner = np.cos(theta_z)*np.cos(beta) + \
        np.sin(theta_z)*np.sin(beta)*np.cos(gamma_s - gamma)

    if is_near(inner, 1, 1E-13):
        inner = 1
    theta = np.arccos(inner)

    # Convert answer to degrees
    theta = np.degrees(theta)

    return theta


def solar_azimuth_angle(omega, theta_z, phi, delta):
    # Convert all degrees to radians
    omega = np.radians(omega)
    theta_z = np.radians(theta_z)
    phi = np.radians(phi)
    delta = np.radians(delta)

    gamma_s = np.arccos((np.cos(theta_z)*np.sin(phi) - np.sin(delta)) /
                        (np.sin(theta_z)*np.cos(phi)))
    gamma_s = math.copysign(gamma_s, omega)

    gamma_s = np.degrees(gamma_s)

    return gamma_s


def solar_time(Loc, Lst, E, stand_time):
    solar_time_min = stand_time.minute + 4*(Lst - Loc) - E
    if solar_time_min > 59:
        solar_time_min -= 60
        carryover = 1
    elif solar_time_min < 0:
        solar_time_min += 60
        carryover = -1
    else:
        carryover = 0

    solar_time_min = int(solar_time_min)
    solar_time = datetime.time(stand_time.hour + carryover, solar_time_min, 0)

    return solar_time


def zenith_angle(phi, delta, omega):
    """
    Parameters:
        phi - Latitude
        delta - Declination Angle
        omega - Hour Angle
    """

    # Convert all degrees to radians
    phi = np.radians(phi)
    delta = np.radians(delta)
    omega = np.radians(omega)

    theta_z = np.arccos(np.cos(phi)*np.cos(delta)*np.cos(omega) +
                        np.sin(phi)*np.sin(delta))

    theta_z = np.degrees(theta_z)
    return theta_z
