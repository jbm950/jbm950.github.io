import datetime
import funcs
import matplotlib.pyplot as plt
import numpy as np

Gsc = 1367
Gon = Gsc * (1+0.033*np.cos(360/365*172))

stand_times = []
for i in range(4, 20):
    for j in range(60):
        stand_times += [datetime.time(i, j, 0)]

solarsolstice = datetime.date(2016, 6, 21)
times = [datetime.datetime.combine(solarsolstice, i) for i in stand_times]

Loc = 82.13
phi = 29.7
Lst = 75
E = -1.33
delta = 23.45

solartimes = [funcs.solar_time(Loc, Lst, E, i) for i in stand_times]
hour_angles = [funcs.hour_angle(i) for i in solartimes]
thetazs = [funcs.zenith_angle(phi, delta, i) for i in hour_angles]
gammas = [funcs.solar_azimuth_angle(hour_angles[i], thetazs[i], phi, delta) for
          i in range(len(hour_angles))]
betas = thetazs
gamma = gammas
thetas = [funcs.incidence_angle(thetazs[i], betas[i], gammas[i], gamma[i]) for i
          in range(len(thetazs))]
thetas = np.radians(np.array(thetas))

Gbt = [np.cos(i)*Gon for i in thetas]

thetas2 = [funcs.incidence_angle(thetazs[i], phi, gammas[i], 0) for i in
           range(len(thetazs))]
thetas2 = np.radians(np.array(thetas2))
Gbt2 = [np.cos(i)*Gon for i in thetas2]

plt.plot(times, Gbt, times, Gbt2)
plt.xlabel("Time of Day (Local Time)")
plt.ylabel("Beam Irradiance on a Tilted Surface W/m^2")
plt.title("Irradiance Recieved by a Surface during the Summer Solstice")
plt.legend(["2-D Tracking System", "Stationary Surface (slope = latitude)"],
           loc=4)
plt.show()
