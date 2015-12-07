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

        P6orig_F = (Ptool_F - np.dot(Pt6, x)[0] * a67_F - np.dot(Pt6, y)[0] *
                    np.cross(S6_F.transpose(), a67_F.transpose()).transpose() -
                    np.dot(Pt6, z)[0] * S6_F)

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
    Y = -(m.sin(alphas[alpha2]) * m.cos(alphas[alpha1]) +
          m.cos(alphas[alpha2]) * m.sin(alphas[alpha1]) * m.cos(theta))
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
    if len(thetas) == 1:
        if thetas[-1][0] == len(alphas) or (the[0] == len(alphas) and
                                            thetas[-1][0] == 1):
            if thetas[0][0] > the[0]:
                bar = 0
            else:
                bar = 1
        else:
            if thetas[0][0] < the[0]:
                bar = 0
            else:
                bar = 1

        [X_prev, Y_prev, Z_prev] = single_sub(alphas, thetas[0][0],
                                              thetas[0][1], bar)
    else:
        [X_prev, Y_prev, Z_prev] = multi_sub_S(alphas, thetas[:])

    # Convert the remaining degree values to radians for calculation
    alphas = np.array(alphas)

    alphas = np.radians(alphas)
    theta = np.radians(the[1])

    # Determine the actual alpha value to be used in calculations
    if thetas[-1][0] == len(alphas) or (the[0] == len(alphas) and
                                        thetas[-1][0] == 1):
        if thetas[-1][0] > the[0]:
            alpha = alphas[the[0] - 1]
        else:
            alpha = alphas[the[0] - 2]
    else:
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
        """The joint offsets will be defined for this specific robot"""
        link_lengths = [0, 70, 90, 0, 0]
        twist_angles = [270, 0, 0, 270, 90]

        Robot_6link.__init__(self, link_lengths, twist_angles)

        # joint_offsets = [S1, S2, S3, S4, S5, S6, S7] where S1 and S7 will be
        # determined during reverse analysis while performing the close the loop
        # step. The value for S6 is decided to be 15.24 cm

        joint_offsets = [0, 0, 0, 9.8, 14.5, 15.24, 0]
        self.joint_offsets = np.array(joint_offsets)

    def reverse_analysis(self, Ptool_6, Ptool_F, S6_F, a67_F):
        """This function will perform the reverse analysis for this mechanism
        and provide the joint angles for each joint of the robot"""

        # First determine the close the loop values
        [S7, a71, S1, theta7, alp71, gamma1] = close_the_loop(S6_F, a67_F,
                                                              Ptool_F, Ptool_6)

        # Fill in the state parameters arrays
        self.joint_offsets[0] = S1
        self.joint_offsets[6] = S7

        self.link_lengths = np.append(self.link_lengths, 0)
        self.link_lengths = np.append(self.link_lengths, a71)

        self.twist_angles = np.append(self.twist_angles, m.radians(90))
        self.twist_angles = np.append(self.twist_angles, m.radians(alp71))
        twist_anglesd = np.degrees(self.twist_angles)

        # The next step will be to obtain theta1
        [X7, Y7, Z7] = single_sub(twist_anglesd, 7, theta7, 0)
        # A, B and D from eqn 11.55 in the book
        A = (- self.joint_offsets[5] * Y7 + self.joint_offsets[6] *
             m.sin(self.twist_angles[6]))
        B = (- self.joint_offsets[5] * X7 - self.link_lengths[6])
        D = self.joint_offsets[3]
        [worked, theta1A, theta1B] = trig_solution(A, B, D)

        # The next angle to be obtained will be theta5 and eqn 11.58 from the
        # book will be used
        [X17A, Y17A, Z17A] = multi_sub_S(twist_anglesd, [[1, theta1A],
                                                         [7, theta7]])
        theta5AA = np.arccos(Z17A)
        theta5AB = - theta5AA

        [X17B, Y17B, Z17B] = multi_sub_S(twist_anglesd, [[1, theta1B],
                                                         [7, theta7]])
        theta5BA = np.arccos(Z17B)
        theta5BB = - theta5BA

        # Convert theta5 to degrees
        theta5AA = m.degrees(theta5AA)
        theta5AB = m.degrees(theta5AB)
        theta5BA = m.degrees(theta5BA)
        theta5BB = m.degrees(theta5BB)

        # The next angle to be obtained will be theta6 and eqns 11.67 and 11.68
        # will be used for this purpose along with the 4 quadrant arctan
        c_6AA = - X17A / m.sin(m.radians(theta5AA))
        s_6AA = Y17A / m.sin(m.radians(theta5AA))
        theta6AA = np.arctan2(s_6AA, c_6AA)

        c_6AB = - X17A / m.sin(m.radians(theta5AB))
        s_6AB = Y17A / m.sin(m.radians(theta5AB))
        theta6AB = np.arctan2(s_6AB, c_6AB)

        c_6BA = - X17B / m.sin(m.radians(theta5BA))
        s_6BA = Y17B / m.sin(m.radians(theta5BA))
        theta6BA = np.arctan2(s_6BA, c_6BA)

        c_6BB = - X17B / m.sin(m.radians(theta5BB))
        s_6BB = Y17B / m.sin(m.radians(theta5BB))
        theta6BB = np.arctan2(s_6BB, c_6BB)

        # Convert theta6 to degrees
        theta6AA = m.degrees(theta6AA)
        theta6AB = m.degrees(theta6AB)
        theta6BA = m.degrees(theta6BA)
        theta6BB = m.degrees(theta6BB)

        # Next angle to be found is theta3 and first the K1 and K2 values from
        # eqns 11.76 and 11.77 will be determined and will be used in eqn 11.89
        [X671AA, Y671AA, Z671AA] = multi_sub_S(twist_anglesd, [[6, theta6AA],
                                                               [7, theta7],
                                                               [1, theta1A]])
        [X671AB, Y671AB, Z671AB] = multi_sub_S(twist_anglesd, [[6, theta6AB],
                                                               [7, theta7],
                                                               [1, theta1A]])
        [X671BA, Y671BA, Z671BA] = multi_sub_S(twist_anglesd, [[6, theta6BA],
                                                               [7, theta7],
                                                               [1, theta1B]])
        [X671BB, Y671BB, Z671BB] = multi_sub_S(twist_anglesd, [[6, theta6BB],
                                                               [7, theta7],
                                                               [1, theta1B]])
        [X71A, Y71A, Z71A] = multi_sub_S(twist_anglesd, [[7, theta7],
                                                         [1, theta1A]])
        [X71B, Y71B, Z71B] = multi_sub_S(twist_anglesd, [[7, theta7],
                                                         [1, theta1B]])
        [X1A, Y1A, Z1A] = single_sub(twist_anglesd, 1, theta1A, 0)
        [X1B, Y1B, Z1B] = single_sub(twist_anglesd, 1, theta1B, 0)

        K1AA = (-self.joint_offsets[4] * X671AA - self.joint_offsets[5] * X71A -
                self.joint_offsets[6] * X1A - self.link_lengths[6] *
                m.cos(m.radians(theta1A)))
        K1AB = (-self.joint_offsets[4] * X671AB - self.joint_offsets[5] * X71A -
                self.joint_offsets[6] * X1A - self.link_lengths[6] *
                m.cos(m.radians(theta1A)))
        K1BA = (-self.joint_offsets[4] * X671BA - self.joint_offsets[5] * X71B -
                self.joint_offsets[6] * X1B - self.link_lengths[6] *
                m.cos(m.radians(theta1B)))
        K1BB = (-self.joint_offsets[4] * X671BB - self.joint_offsets[5] * X71B -
                self.joint_offsets[6] * X1B - self.link_lengths[6] *
                m.cos(m.radians(theta1B)))

        K2AA = (-self.joint_offsets[0] - self.joint_offsets[4] * Y671AA -
                self.joint_offsets[5] * Y71A - self.joint_offsets[6] * Y1A)
        K2AB = (-self.joint_offsets[0] - self.joint_offsets[4] * Y671AB -
                self.joint_offsets[5] * Y71A - self.joint_offsets[6] * Y1A)
        K2BA = (-self.joint_offsets[0] - self.joint_offsets[4] * Y671BA -
                self.joint_offsets[5] * Y71B - self.joint_offsets[6] * Y1B)
        K2BB = (-self.joint_offsets[0] - self.joint_offsets[4] * Y671BB -
                self.joint_offsets[5] * Y71B - self.joint_offsets[6] * Y1B)

        theta3AAA = np.arccos((K1AA**2 + K2AA**2 - self.link_lengths[1]**2 -
                               self.link_lengths[2]**2) /
                              (2 * self.link_lengths[1] * self.link_lengths[2]))
        theta3AAB = - theta3AAA

        theta3ABA = np.arccos((K1AB**2 + K2AB**2 - self.link_lengths[1]**2 -
                               self.link_lengths[2]**2) /
                              (2 * self.link_lengths[1] * self.link_lengths[2]))
        theta3ABB = - theta3ABA

        theta3BAA = np.arccos((K1BA**2 + K2BA**2 - self.link_lengths[1]**2 -
                               self.link_lengths[2]**2) /
                              (2 * self.link_lengths[1] * self.link_lengths[2]))
        theta3BAB = - theta3BAA

        theta3BBA = np.arccos((K1BB**2 + K2BB**2 - self.link_lengths[1]**2 -
                               self.link_lengths[2]**2) /
                              (2 * self.link_lengths[1] * self.link_lengths[2]))
        theta3BBB = - theta3BBA

        # Convert theta3 to degrees
        theta3AAA = m.degrees(theta3AAA)
        theta3AAB = m.degrees(theta3AAB)
        theta3ABA = m.degrees(theta3ABA)
        theta3ABB = m.degrees(theta3ABB)
        theta3BAA = m.degrees(theta3BAA)
        theta3BAB = m.degrees(theta3BAB)
        theta3BBA = m.degrees(theta3BBA)
        theta3BBB = m.degrees(theta3BBB)

        # The second to last angle to find will be theta2. The system of
        # equations Ax = b will be used using eqns 11.90 and 11.91
        A_AAA = np.matrix([[self.link_lengths[1] + self.link_lengths[2] *
                            m.cos(m.radians(theta3AAA)), -self.link_lengths[2] *
                            m.sin(m.radians(theta3AAA))],
                           [-self.link_lengths[2] * m.sin(m.radians(theta3AAA)),
                            -self.link_lengths[1] - self.link_lengths[2] *
                            m.cos(m.radians(theta3AAA))]])
        A_AAB = np.matrix([[self.link_lengths[1] + self.link_lengths[2] *
                            m.cos(m.radians(theta3AAB)), -self.link_lengths[2] *
                            m.sin(m.radians(theta3AAB))],
                           [-self.link_lengths[2] * m.sin(m.radians(theta3AAB)),
                            -self.link_lengths[1] - self.link_lengths[2] *
                            m.cos(m.radians(theta3AAB))]])
        b_AA = np.matrix([[K1AA], [K2AA]])

        A_ABA = np.matrix([[self.link_lengths[1] + self.link_lengths[2] *
                            m.cos(m.radians(theta3ABA)), -self.link_lengths[2] *
                            m.sin(m.radians(theta3ABA))],
                           [-self.link_lengths[2] * m.sin(m.radians(theta3ABA)),
                            -self.link_lengths[1] - self.link_lengths[2] *
                            m.cos(m.radians(theta3ABA))]])
        A_ABB = np.matrix([[self.link_lengths[1] + self.link_lengths[2] *
                            m.cos(m.radians(theta3ABB)), -self.link_lengths[2] *
                            m.sin(m.radians(theta3ABB))],
                           [-self.link_lengths[2] * m.sin(m.radians(theta3ABB)),
                            -self.link_lengths[1] - self.link_lengths[2] *
                            m.cos(m.radians(theta3ABB))]])
        b_AB = np.matrix([[K1AB], [K2AB]])

        A_BAA = np.matrix([[self.link_lengths[1] + self.link_lengths[2] *
                            m.cos(m.radians(theta3BAA)), -self.link_lengths[2] *
                            m.sin(m.radians(theta3BAA))],
                           [-self.link_lengths[2] * m.sin(m.radians(theta3BAA)),
                            -self.link_lengths[1] - self.link_lengths[2] *
                            m.cos(m.radians(theta3BAA))]])
        A_BAB = np.matrix([[self.link_lengths[1] + self.link_lengths[2] *
                            m.cos(m.radians(theta3BAB)), -self.link_lengths[2] *
                            m.sin(m.radians(theta3BAB))],
                           [-self.link_lengths[2] * m.sin(m.radians(theta3BAB)),
                            -self.link_lengths[1] - self.link_lengths[2] *
                            m.cos(m.radians(theta3BAB))]])
        b_BA = np.matrix([[K1BA], [K2BA]])

        A_BBA = np.matrix([[self.link_lengths[1] + self.link_lengths[2] *
                            m.cos(m.radians(theta3BBA)), -self.link_lengths[2] *
                            m.sin(m.radians(theta3BBA))],
                           [-self.link_lengths[2] * m.sin(m.radians(theta3BBA)),
                            -self.link_lengths[1] - self.link_lengths[2] *
                            m.cos(m.radians(theta3BBA))]])
        A_BBB = np.matrix([[self.link_lengths[1] + self.link_lengths[2] *
                            m.cos(m.radians(theta3BBB)), -self.link_lengths[2] *
                            m.sin(m.radians(theta3BBB))],
                           [-self.link_lengths[2] * m.sin(m.radians(theta3BBB)),
                            -self.link_lengths[1] - self.link_lengths[2] *
                            m.cos(m.radians(theta3BBB))]])
        b_BB = np.matrix([[K1BB], [K2BB]])

        [c2_AAA, s2_AAA] = np.linalg.solve(A_AAA, b_AA)
        theta2AAA = m.degrees(np.arctan2(s2_AAA, c2_AAA))

        [c2_AAB, s2_AAB] = np.linalg.solve(A_AAB, b_AA)
        theta2AAB = m.degrees(np.arctan2(s2_AAB, c2_AAB))

        [c2_ABA, s2_ABA] = np.linalg.solve(A_ABA, b_AB)
        theta2ABA = m.degrees(np.arctan2(s2_ABA, c2_ABA))

        [c2_ABB, s2_ABB] = np.linalg.solve(A_ABB, b_AB)
        theta2ABB = m.degrees(np.arctan2(s2_ABB, c2_ABB))

        [c2_BAA, s2_BAA] = np.linalg.solve(A_BAA, b_BA)
        theta2BAA = m.degrees(np.arctan2(s2_BAA, c2_BAA))

        [c2_BAB, s2_BAB] = np.linalg.solve(A_BAB, b_BA)
        theta2BAB = m.degrees(np.arctan2(s2_BAB, c2_BAB))

        [c2_BBA, s2_BBA] = np.linalg.solve(A_BBA, b_BB)
        theta2BBA = m.degrees(np.arctan2(s2_BBA, c2_BBA))

        [c2_BBB, s2_BBB] = np.linalg.solve(A_BBB, b_BB)
        theta2BBB = m.degrees(np.arctan2(s2_BBB, c2_BBB))

        # The final angle to find will be theta4 and eqns 11.94 and 11.95 will
        # be used for this purpose
        [X67123AAA, Y67123AAA, Z67123AAA] = multi_sub_S(twist_anglesd,
                                                        [[6, theta6AA],
                                                         [7, theta7],
                                                         [1, theta1A],
                                                         [2, theta2AAA],
                                                         [3, theta3AAA]])
        s4_AAA = - X67123AAA
        c4_AAA = - Y67123AAA
        theta4AAA = m.degrees(np.arctan2(s4_AAA, c4_AAA))

        [X67123AAB, Y67123AAB, Z67123AAB] = multi_sub_S(twist_anglesd,
                                                        [[6, theta6AA],
                                                         [7, theta7],
                                                         [1, theta1A],
                                                         [2, theta2AAB],
                                                         [3, theta3AAB]])
        s4_AAB = - X67123AAB
        c4_AAB = - Y67123AAB
        theta4AAB = m.degrees(np.arctan2(s4_AAB, c4_AAB))

        [X67123ABA, Y67123ABA, Z67123ABA] = multi_sub_S(twist_anglesd,
                                                        [[6, theta6AB],
                                                         [7, theta7],
                                                         [1, theta1A],
                                                         [2, theta2ABA],
                                                         [3, theta3ABA]])
        s4_ABA = - X67123ABA
        c4_ABA = - Y67123ABA
        theta4ABA = m.degrees(np.arctan2(s4_ABA, c4_ABA))

        [X67123ABB, Y67123ABB, Z67123ABB] = multi_sub_S(twist_anglesd,
                                                        [[6, theta6AB],
                                                         [7, theta7],
                                                         [1, theta1A],
                                                         [2, theta2ABB],
                                                         [3, theta3ABB]])
        s4_ABB = - X67123ABB
        c4_ABB = - Y67123ABB
        theta4ABB = m.degrees(np.arctan2(s4_ABB, c4_ABB))

        [X67123BAA, Y67123BAA, Z67123BAA] = multi_sub_S(twist_anglesd,
                                                        [[6, theta6BA],
                                                         [7, theta7],
                                                         [1, theta1B],
                                                         [2, theta2BAA],
                                                         [3, theta3BAA]])
        s4_BAA = - X67123BAA
        c4_BAA = - Y67123BAA
        theta4BAA = m.degrees(np.arctan2(s4_BAA, c4_BAA))

        [X67123BAB, Y67123BAB, Z67123BAB] = multi_sub_S(twist_anglesd,
                                                        [[6, theta6BA],
                                                         [7, theta7],
                                                         [1, theta1B],
                                                         [2, theta2BAB],
                                                         [3, theta3BAB]])
        s4_BAB = - X67123BAB
        c4_BAB = - Y67123BAB
        theta4BAB = m.degrees(np.arctan2(s4_BAB, c4_BAB))

        [X67123BBA, Y67123BBA, Z67123BBA] = multi_sub_S(twist_anglesd,
                                                        [[6, theta6BB],
                                                         [7, theta7],
                                                         [1, theta1B],
                                                         [2, theta2BBA],
                                                         [3, theta3BBA]])
        s4_BBA = - X67123BBA
        c4_BBA = - Y67123BBA
        theta4BBA = m.degrees(np.arctan2(s4_BBA, c4_BBA))

        [X67123BBB, Y67123BBB, Z67123BBB] = multi_sub_S(twist_anglesd,
                                                        [[6, theta6BB],
                                                         [7, theta7],
                                                         [1, theta1B],
                                                         [2, theta2BBB],
                                                         [3, theta3BBB]])
        s4_BBB = - X67123BBB
        c4_BBB = - Y67123BBB
        theta4BBB = m.degrees(np.arctan2(s4_BBB, c4_BBB))

        # Find phi1 values before returning all the solved for values
        phi1A = theta1A - gamma1
        phi1B = 360 + theta1B - gamma1

        # Form a solutions matrix of the different theta values
        phi1s = [phi1A, phi1A, phi1A, phi1A, phi1B, phi1B, phi1B, phi1B]
        theta2s = [theta2AAA, theta2AAB, theta2ABA, theta2ABB,
                   theta2BAA, theta2BAB, theta2BBA, theta2BBB]
        theta3s = [theta3AAA, theta3AAB, theta3ABA, theta3ABB,
                   theta3BAA, theta3BAB, theta3BBA, theta3BBB]
        theta4s = [theta4AAA, theta4AAB, theta4ABA, theta4ABB,
                   theta4BAA, theta4BAB, theta4BBA, theta4BBB]
        theta5s = [theta5AA, theta5AA, theta5AB, theta5AB,
                   theta5BA, theta5BA, theta5BB, theta5BB]
        theta6s = [theta6AA, theta6AA, theta6AB, theta6AB,
                   theta6BA, theta6BA, theta6BB, theta6BB]
        sol = np.array((phi1s, theta2s, theta3s, theta4s, theta5s, theta6s))
        sol = sol.transpose()

        return sol


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
