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


# Reverse Analysis

def close_the_loop(S6_F, a67_F, Ptool_F, Ptool_6):
    """This function will provide 3 distances (S7, a71 and S1) and three
    angles (theta7, alpha71 and gamma1)
    Inputs:
        S6_F - This is the orientation of the unit vector S6 in the fixed
            coordinate system
        a67_F - This is the orientation of the unit vector a67 in the fixed
            coordinate system
        Ptool_F - This is the location of the tool point in the fixed
            coordinate system
        Ptool_6 - This is the location of the tool point in the 6th
            coordinate system"""

    # Function to take care of special case 1
    def special_case_1():
        pass

    # Function to take care of special case 2
    def special_case_2():
        pass

    # Define some constants and create numpy arrays of the inputs.
    S1_F = np.matrix([[0], [0], [1]])
    x1_F = np.matrix([[1], [0], [0]])
    S6_F = np.matrix(S6_F)
    a67_F = np.matrix(a67_F)
    Ptool_F = np.matrix(Ptool_F)
    Ptool_6 = np.matrix(Ptool_6)

    # Find the origin of the 6th coordinate system in the fixed coordinate
    # system
    def find_P6orig_F(Ptool_6, Ptool_F, a67_F, S6_F):
        x = np.array([1, 0, 0])
        y = np.array([0, 1, 0])
        z = np.array([0, 0, 1])
        Pt6 = Ptool_6.transpose()
        Pt6 = np.array(Pt6)

        P6orig_F = (Ptool_F - np.dot(Pt6, x)[0] * a67_F - np.dot(Pt6, y)[0]
                    * np.cross(S6_F.transpose(), a67_F.transpose()).transpose()
                    - np.dot(Pt6, z)[0] * S6_F)

        return P6orig_F

    P6orig_F = find_P6orig_F(Ptool_6, Ptool_F, a67_F, S6_F)

    # Make free choice about length a67 and angle alpha67
    # a67 = 0
    # alp67 = m.radians(90)

    # Find the orientation of vector S7 in the fixed coordinate system
    S7_F = np.cross(a67_F.transpose(), S6_F.transpose())

    # Fist determine is there will be any problems and a special case needed
    if is_near(m.fabs(np.dot(S7_F, S1_F)), 1, 0.001):
        special_case_1()
    else:

        # Find the vector a71_F
        interval = np.cross(S7_F, S1_F.transpose())
        a71_F = interval/(np.linalg.norm(interval))

        # Find the cosine and sine components of alpha 71 and use arctan2 to
        # find the angle
        c71 = np.dot(S7_F, S1_F)
        s71 = np.dot(np.cross(S7_F, S1_F.transpose()), a71_F.transpose())
        alp71 = np.arctan2(s71, c71)

        # Find the cosine and sine components of gamma 1 and use arctan2 to
        # find the angle
        c7 = np.dot(a67_F.transpose(), a71_F.transpose())
        s7 = np.dot(np.cross(a67_F.transpose(), a71_F), S7_F.transpose())
        theta7 = np.arctan2(s7, c7)

        # Find the cosine and sine components of gamma 1 and use arctan2 to
        # find the angle
        c_gamma_1 = np.dot(a71_F, x1_F)
        s_gamma_1 = np.dot(np.cross(a71_F, x1_F.transpose()),
                           S1_F)
        gamma1 = np.arctan2(s_gamma_1, c_gamma_1)

        # Now find the length S7
        S7 = (np.dot(np.cross(S1_F.transpose(), P6orig_F.transpose()),
                     a71_F.transpose()))/m.sin(alp71)

        # Now find the length a71
        a71 = (np.dot(np.cross(P6orig_F.transpose(), S1_F.transpose()),
                      S7_F.transpose()))/m.sin(alp71)

        # Lastly find the length S1
        S1 = (np.dot(np.cross(P6orig_F.transpose(), S7_F),
                     a71_F.transpose()))/m.sin(alp71)

    # Prepare the returned variables
    S7 = S7[0][0]
    a71 = a71[0][0]
    S1 = S1[0][0]
    theta7 = m.degrees(theta7[0][0])
    alp71 = m.degrees(alp71[0][0])
    gamma1 = m.degrees(gamma1[0][0])

    return S7, a71, S1, theta7, alp71, gamma1


def trig_solution(A, B, D):
    """This function will solve equations of the following form
            Acos(1) + Bsin(1) + D = 0
    Inputs:
        A - This is the coefficient of the cos term
        B - This is the coefficient of the sin term
        D - This is the constant term in the equation"""

    # Begin by finding the imaginary angle gamma
    c_gam = A/m.sqrt(A**2 + B**2)
    s_gam = B/m.sqrt(A**2 + B**2)
    gamma = np.arctan2(s_gam, c_gam)

    # Now find the intermediate term cos(1 - gamma) and test whether or not
    # real angles will be produced
    interval = -D/m.sqrt(A**2 + B**2)
    if m.fabs(interval) > 1:
        return 0, 0, 0

    # Given that the theta value must exist at this point find the theta values
    thetaA = np.arccos(interval) + gamma
    thetaB = -np.arccos(interval) + gamma

    # Format the return values to degrees
    thetaA = m.degrees(thetaA)
    thetaB = m.degrees(thetaB)

    return 1, thetaA, thetaB


# Short Hand Notation

def single_sub(alphas, subscript, theta, bar):
    """This function will find the X, Y and Z values for single subscript
    notation.
    Inputs:
        alphas - This is a list of the twist angles for the spherical mechanism
            with n links in degrees and listed as follows.
            [alp12, alp23, ..., alpn1]
        subscript - This is the specific subscript that is desired to be found
        theta - This is the theta value that corresponds to the subscript in
            degrees
        bar - This indicates whether or not a bar is included over the terms
            bars -> bar  = 1 otherwise bar = 0"""

    # Change appropriate inputs to numpy arrays and convert degree inputs to
    # radians
    alphas = np.array(alphas)

    alphas = np.radians(alphas)
    theta = np.radians(theta)

    # Define the order of the alphas based on the presence of a bar
    if bar:
        alpha1 = subscript - 1
        alpha2 = subscript - 2
    else:
        alpha1 = subscript - 2
        alpha2 = subscript - 1

    # Find the X, Y and Z terms
    X = m.sin(alphas[alpha1]) * m.sin(theta)
    Y = -(m.sin(alphas[alpha2]) * m.cos(alphas[alpha1]) + m.cos(alphas[alpha2])
          * m.sin(alphas[alpha1]) * m.cos(theta))
    Z = (m.cos(alphas[alpha2]) * m.cos(alphas[alpha1]) - m.sin(alphas[alpha2]) *
         m.sin(alphas[alpha1]) * m.cos(theta))

    return X, Y, Z


def multi_sub_S(alphas, thetas):
    """This function will find the X, Y and Z values for multi-subscript
    notation.
    Inputs:
        alphas - This is a list of the twist angles for the spherical mechanism
            with n links in degrees and listed as follows.
            [alp12, alp23, ..., alpn1]
        thetas - This will be a list with nested subscript/theta value pairs
            where the theta values are measured in degrees
            [[1, the1], [2, the2]] for X_12, Y_12 and Z_12"""

    # First remove the last theta from the list
    the = thetas.pop()

    # Now determine the X, Y and Z values for all of the smaller subscripts
    # Test to see if the next set of subscript values are single subscripts
    if len(thetas) == 2:
        if thetas[0][0] < the[0]:
            bar = 0
        else:
            bar = 1

        [X_prev, Y_prev, Z_prev] = single_sub(alphas, thetas[0][0],
                                              thetas[0][1], bar)
    else:
        [X_prev, Y_prev, Z_prev] = multi_sub_S(alphas, thetas)

    # Convert the remaining degree values to radians for calculation
    alphas = np.array(alphas)

    alphas = np.radians(alphas)
    theta = np.radians(the[1])

    # Determine the actual alpha value to be used in calculations
    if thetas[-1][0] < the[0]:
        alpha = alphas[the[0] - 1]
    else:
        alpha = alphas[the[0] - 2]

    # Now finally calculate and return the desired multi-subscript values
    X = X_prev * m.cos(theta) - Y_prev * m.sin(theta)
    Y = (m.cos(alpha) * (X_prev * m.sin(theta) + Y_prev * m.cos(theta)) -
         m.sin(alpha) * Z_prev)
    Z = (m.sin(alpha) * (X_prev * m.sin(theta) + Y_prev * m.cos(theta)) +
         m.cos(alpha) * Z_prev)

    return X, Y, Z


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


# Other functions

def is_near(value, goal, tolerance):
    """This will determine if two values are the same within a given tolerance
    Inputs:
        value - This is the value you want to test against a set value
        goal - This is the number you are testing to see if value is the same as
        tolerance - This is the amount of distance value can be away from goal
            and still be considered the same"""

    if (goal - tolerance) < value and (goal + tolerance) > value:
        return True
    else:
        return False
