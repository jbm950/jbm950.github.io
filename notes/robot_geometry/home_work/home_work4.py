# This file will contain the computations required for the second homework

import rg_tools as rgt

class GE_P60(rgt.Robot_6link):
    def __init__(self):
        link_lengths = [0, 70, 90, 0, 0]
        twist_angles = [270, 0, 0, 270, 90]

        rgt.Robot_6link.__init__(self, link_lengths, twist_angles)
