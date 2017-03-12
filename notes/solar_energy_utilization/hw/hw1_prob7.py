import funcs
from scipy.optimize import minimize

print("\nProblem 7, Summer Solstice 8:00")
temp_func = lambda beta: funcs.incidence_angle(53.4, beta, 98.5, 0)

print('\tBeta =', minimize(temp_func, 30).x[0], 'degrees\n')

print("Problem 7, Winter Solstice 8:00")
temp_func = lambda beta: funcs.incidence_angle(78.3, beta, 54.2, 0)

print('\tBeta =', minimize(temp_func, 30).x[0], 'degrees\n')
