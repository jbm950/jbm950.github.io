# This file will contain useful code, functions and classes for the robot
# geometry class

import numpy as np
import math as m

# Coordinate Transformations


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
    my = (R_1_2[0, 2] - R_1_2[2, 0]) / (2 * m.sin(theta))
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


# 6 Link Robot Base Class

class Robot_6link:
    def __init__(self, link_lengths, twist_angles):
        """This will be the standard base class for 6 link robots
        Inputs:
            link_lengths - This is a list of all the link lengths in the order
                [a12, a23, a34, a45, a56]
            twist_angles - This is a list of all the twist angles in the order
                [alp12, alp23, alp34, alp45, alp56] all angles in degrees"""

        # Make the inputs into numpy arrays
        self.link_lengths = np.array(link_lengths)
        self.twist_angles = np.array(twist_angles)

        # Convert the twist angles to radians
        self.twist_angles = np.radians(self.twist_angles)

    def forward_analysis(self, joint_offsets, joint_angles, Ptool6):
        """This function will take in the different robot parameters and joint
        angles and determine the location of the tool point in the fixed
        coordinate system
        Inputs:
            joint_offsets - This is a list containing all of the joint offsets
                [S2, S3, S4, S5, S6]
            joint_angles - This is a list containing all of the joint angles
                [phi1, the2, the3, the4, the5, the6] all angles in degrees
            Ptool6 - This is the location of the tool point in the 6th
                coordinate system"""

        # Make the inputs into numpy arrays
        joint_offsets = np.array(joint_offsets)
        joint_angles = np.array(joint_angles)
        Ptool6 = np.matrix(Ptool6 + [1]).transpose()

        # Convert the joint angles to radians
        joint_angles = np.radians(joint_angles)

        # Set up the first transformation matrix
        R_F_1 = rotation_about_z(m.degrees(joint_angles[0]))
        P_1o = np.matrix([[0], [0], [0]])
        T_F_1 = trans_matrix_form(R_F_1, P_1o)

        # Isolate the calculation because it does some extra variable
        # definitions
        def trans_F_6_find(joint_angles, joint_offsets, T_F_1):
            # Short hand notation of previous variables for ease in calculations
            T_F_6 = T_F_1
            ja = joint_angles
            jo = joint_offsets
            ta = self.twist_angles
            ll = self.link_lengths
            c = m.cos
            s = m.sin

            for i in range(0, 5):
                # print("joint angle\n", m.degrees(ja[i+1]))
                # print("joint offset\n", jo[i])
                # print("twist angle\n", m.degrees(ta[i]), "\n")
                R_inter = np.matrix([
                    [c(ja[i+1]),         -s(ja[i+1]),           0],
                    [s(ja[i+1])*c(ta[i]), c(ja[i+1])*c(ta[i]), -s(ta[i])],
                    [s(ja[i+1])*s(ta[i]), c(ja[i+1])*s(ta[i]),  c(ta[i])]])
                P_inter = np.matrix([[ll[i]],
                                     [-s(ta[i])*jo[i]],
                                     [c(ta[i])*jo[i]]])
                T_inter = trans_matrix_form(R_inter, P_inter)
                T_F_6 *= T_inter

            return T_F_6

        # Find the transformation matrix from the 6th to the fixed coordinate
        # system
        T_F_6 = trans_F_6_find(joint_angles, joint_offsets, T_F_1)

        # Use the transformation matrix to return PtoolF, S6 in the F and a67 in
        # the F
        R_F_6 = np.matrix(T_F_6[0:3, 0:3])
        a67_F = np.matrix(R_F_6[0:3, 0])
        S6_F = np.matrix(R_F_6[0:3, 2])
        PtoolF = T_F_6 * Ptool6

        # Change PtoolF back to cartesian coordinates
        PtoolF = np.matrix(PtoolF[0:3])

        return a67_F, S6_F, PtoolF


# Specific 6 Link Robots

class T3_776(Robot_6link):
    def __init__(self):
        link_lengths = [0, 44, 0, 0, 0]
        twist_angles = [90, 0, 90, 61, 61]

        Robot_6link.__init__(self, link_lengths, twist_angles)


class GE_P60(Robot_6link):
    def __init__(self):
        link_lengths = [0, 70, 90, 0, 0]
        twist_angles = [270, 0, 0, 270, 90]

        Robot_6link.__init__(self, link_lengths, twist_angles)
