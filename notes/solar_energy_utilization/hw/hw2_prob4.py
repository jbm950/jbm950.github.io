from scipy.integrate import simps

GHI = [64, 153, 245, 335, 416, 486, 543, 585, 474, 623, 618, 596, 559, 507, 441,
       364, 278, 187, 100]
times = [1800*i for i in range(len(GHI))]

H = simps(GHI, times)
print("H = %.1f\n" % H)

DHI = [35, 51, 63, 71, 78, 83, 86, 89, 259, 91, 90, 89, 87, 83, 79, 72, 64, 52,
       44]

Hd = simps(DHI, times)
print("Hd = %.1f\n" % Hd)

print("Hb = %.1f\n" % (H-Hd))
