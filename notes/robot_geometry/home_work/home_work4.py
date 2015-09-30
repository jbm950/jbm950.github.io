# This file will contain the computations required for the second homework

import rg_tools as rgt


class GE_P60(rgt.Robot_6link):
    def __init__(self):
        link_lengths = [0, 70, 90, 0, 0]
        twist_angles = [270, 0, 0, 270, 90]

        rgt.Robot_6link.__init__(self, link_lengths, twist_angles)

class T3_776(rgt.Robot_6link):
    def __init__(self):
        pass

A = GE_P60()
A.joint_angles = [50, 120, 295, 30, 190, 100]
A.joint_offsets = [0, 0, 9.8, 14.5, 6]
A.Ptool6 = [12, 8, 5]

[A.a67_F, A.S6_F, A.PtoolF] = A.forward_analysis(A.joint_offsets,
                                                 A.joint_angles, A.Ptool6)

print("GE P60\n")
print("\ta67_F =\n", A.a67_F, "\n\n")
print("\tS6_F =\n", A.S6_F, "\n\n")
print("\tPtoolF =\n", A.PtoolF, "\n\n")
