# This file will contain useful code, functions and classes for the robot
# geometry class

import numpy as np
import math as m


def rotation_about_x(theta):
    """This function will return the rotation matrix for a rotation theta about
    the x-axis where theta is in degrees"""

    theta = m.radians(theta)

    R_1_2 = np.matrix([[1, 0,             0],
                       [0, m.cos(theta), -m.sin(theta)],
                       [0, m.sin(theta), m.cos(theta)]])

    return R_1_2


def rotation_about_y(theta):
    """This function will return the rotation matrix for a rotation theta about
    the z-axis where theta is in degrees"""

    theta = m.radians(theta)

    R_1_2 = np.matrix([[m.cos(theta), 0, m.sin(theta)],
                       [0,            1, 0],
                       [-m.sin(theta), 0, m.cos(theta)]])

    return R_1_2


def rotation_about_z(theta):
    """This function will return the rotation matrix for a rotation theta about
    the z-axis where theta is in degrees"""

    theta = m.radians(theta)

    R_1_2 = np.matrix([[m.cos(theta), -m.sin(theta), 0],
                       [m.sin(theta), m.cos(theta),  0],
                       [0,            0,             1]])

    return R_1_2


def gen_vec_rotation_matrix(theta, vector):
    """This function will return the rotation matrix for a rotation around a
    given vector (doesn't have to be unit length). The rotation angle theta
    needs to be input in degrees."""

    theta = m.radians(theta)

    m_v = vector/np.linalg.norm(vector)
    mx = m_v[0][0]
    my = m_v[1][0]
    mz = m_v[2][0]
    c = m.cos(theta)
    s = m.sin(theta)
    v = (1-c)

    R_11 = mx * mx * v + c
    R_12 = mx * my * v - mz * s
    R_13 = mx * mz * v + my * s
    R_21 = mx * my * v + mz * s
    R_22 = my * my * v + c
    R_23 = my * mz * v - mx * s
    R_31 = mx * mz * v - my * s
    R_32 = my * mz * v + mx * s
    R_33 = mz * mz * v + c

    R_1_2 = np.matrix([[R_11, R_12, R_13],
                       [R_21, R_22, R_23],
                       [R_31, R_32, R_33]])

    return R_1_2


def rev_gen_vec_rotation_matrix(R_1_2):
    """This function will take a rotation matrix and determine what rotation
    angle will be needed and the vector that is rotated around. Returns theta in
    degrees and the vector m"""

    theta = m.acos((R_1_2[0, 0] + R_1_2[1, 1] + R_1_2[2, 2] - 1) / 2)

    mx = (R_1_2[2, 1] - R_1_2[1, 2]) / (2 * m.sin(theta))
    my = (R_1_2[2, 0] - R_1_2[0, 2]) / (2 * m.sin(theta))
    mz = (R_1_2[1, 0] - R_1_2[0, 1]) / (2 * m.sin(theta))

    m_v = np.matrix([[mx], [my], [mz]])
    theta = m.degrees(theta)

    return [theta, m_v]


def trans_matrix_form(R_1_2, P_2o):
    """This function will return the transformation matrix 2 to 1 given a
    rotation matrix and vector pointing to the origin of system 2 as seen in
    system 1"""

    T_1_2 = np.matrix([[R_1_2[0, 0], R_1_2[0, 1], R_1_2[0, 2], P_2o[0, 0]],
                       [R_1_2[1, 0], R_1_2[1, 1], R_1_2[1, 2], P_2o[1, 0]],
                       [R_1_2[2, 0], R_1_2[2, 1], R_1_2[2, 2], P_2o[2, 0]],
                       [0,           0,           0,           1]])

    return T_1_2


def inv_trans_matrix(trans_matrix):
    """This function will invert the transformation matrix so that it reverses
    the direction of the transformation between coordinate systems"""

    rot_matrix = trans_matrix[0:3, 0:3]
    Porg = trans_matrix[0:3, 3]

    new_rot_matrix = rot_matrix.transpose()
    nrm = new_rot_matrix
    new_Porg = -new_rot_matrix * Porg
    nPo = new_Porg

    new_trans_matrix = np.matrix([[nrm[0, 0], nrm[0, 1], nrm[0, 2], nPo[0, 0]],
                                  [nrm[1, 0], nrm[1, 1], nrm[1, 2], nPo[1, 0]],
                                  [nrm[2, 0], nrm[2, 1], nrm[2, 2], nPo[2, 0]],
                                  [0,         0,         0,         1]])
    return new_trans_matrix
