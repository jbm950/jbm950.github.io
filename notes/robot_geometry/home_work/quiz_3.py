import rg_tools as rgt

m1 = [8, 4, 6]
the1 = 60

r = rgt.Quaternion([0, 1, 0, 0])
q1 = rgt.Quaternion.compose(m1, the1)
q1inv = q1.inv()

m2 = (q1*r*q1inv).numbers[1:4]
the2 = 76

q2 = rgt.Quaternion.compose(m2, the2)
q2inv = q2.inv()

m3 = [0, 1, 0]
the3 = 50

q3 = rgt.Quaternion.compose(m3, the3)
q3inv = q3.inv()

q4 = q1inv * q2inv * q3inv
print(q4.numbers)
print(q4.decompose())
