import numpy as np
import rg_tools as rgt

s = [8, 4, 6]
theta = 60

r = rgt.Quaternion([0, 1, 2, 3])
q = rgt.Quaternion.compose(s, theta)
qinv = q.inv()

rprime = q * r * qinv
print(rprime.numbers)
