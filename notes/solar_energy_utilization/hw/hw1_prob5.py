import datetime
import funcs
import matplotlib.pyplot as plt

stand_times = []
for i in range(4, 20):
    for j in range(60):
        stand_times += [datetime.time(i, j, 0)]


def solartime_1(stand_time):
    Loc = 82.13
    Lst = 75
    E = -1.33

    solar_time_min = stand_time.minute + 4*(Lst - Loc) - E
    if solar_time_min > 59:
        solar_time_min -= 60
        carryover = 1
    elif solar_time_min < 0:
        solar_time_min += 60
        carryover = -1
    else:
        carryover = 0

    solar_time_min = int(solar_time_min)
    solar_time = datetime.time(stand_time.hour + carryover, solar_time_min, 0)

    return solar_time


def solartime_2(stand_time):
    Loc = 82.13
    Lst = 75
    E = -1.33

    solar_time_min = stand_time.minute + 4*(Lst - Loc) - E
    if solar_time_min > 59:
        solar_time_min -= 60
        carryover = 1
    elif solar_time_min < 0:
        solar_time_min += 60
        carryover = -1
    else:
        carryover = 0

    solar_time_min = int(solar_time_min)
    solar_time = datetime.time(stand_time.hour + carryover, solar_time_min, 0)

    return solar_time

solartimes1 = [solartime_1(i) for i in stand_times]
solartimes2 = [solartime_2(i) for i in stand_times]

hour_angles1 = [funcs.hour_angle(i) for i in solartimes1]
hour_angles2 = [funcs.hour_angle(i) for i in solartimes2]

delta1 = 23.45
delta2 = -23.45
phi = 29.7
gamma = 0
beta = 29.7

thetazs_1 = [funcs.zenith_angle(phi, delta1, i) for i in hour_angles1]
thetazs_2 = [funcs.zenith_angle(phi, delta2, i) for i in hour_angles2]

gammas1 = [funcs.solar_azimuth_angle(hour_angles1[i], thetazs_1[i], phi, delta1)
           for i in range(len(hour_angles1))]
gammas2 = [funcs.solar_azimuth_angle(hour_angles2[i], thetazs_2[i], phi, delta2)
           for i in range(len(hour_angles2))]

thetas1 = [funcs.incidence_angle(thetazs_1[i], beta, gammas1[i], gamma) for i in
           range(len(thetazs_1))]
thetas2 = [funcs.incidence_angle(thetazs_2[i], beta, gammas2[i], gamma) for i in
           range(len(thetazs_2))]

solarsolstice = datetime.date(2016, 6, 21)
times = [datetime.datetime.combine(solarsolstice, i) for i in stand_times]

plt.plot(times, thetas1, times, thetas2)
plt.xlabel("Time of Day (Local Time)")
plt.ylabel("Inclination Angle (theta)")
plt.title("Inclination Angle on Winter and Solar Solstices in Gainesville, FL")
plt.legend(["Solar Solstice", "Winter Solstice"])
plt.show()
