from scipy.optimize import bisect

G_T = 1000
alpha = 0.9
tau = 0.9
T_s = 273
e_a = 0.8
T_a = 50+273
e_c = 0.5
h_abs_cov = 2
h_above_cov = 10
sigma = 5.67E-8


# Part a, b
def R_1(T_c):
    num = (T_a - T_c)*(1/e_a + 1/e_c - 1)
    denom = sigma*(T_a**4 - T_c**4) + h_abs_cov*(T_a - T_c)*(1/e_a + 1/e_c - 1)
    return num/denom


def R_2(T_c):
    num = T_c - T_s
    denom = sigma*e_c*(T_c**4 - T_s**4) + h_above_cov*(T_c - T_s)
    return num/denom


def func(T_c):
    return (T_a - T_s)/(R_1(T_c) + R_2(T_c)) - (T_c - T_s)/R_2(T_c)

# Part a
T_c = bisect(func, T_s+0.1, T_a-0.1)
U_L = 1/(R_1(T_c) + R_2(T_c))
print("T_c = %.3f, U_L = %.3f" % (T_c, U_L))

# Part b
h_abs_cov = 0
T_c = bisect(func, T_s+0.1, T_a-0.1)
U_L = 1/(R_1(T_c) + R_2(T_c))
print("T_c = %.3f, U_L = %.3f" % (T_c, U_L))
