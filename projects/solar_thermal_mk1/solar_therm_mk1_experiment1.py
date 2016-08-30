import csv
import matplotlib.pyplot as plt
import numpy as np

with open("solar_therm_mk1_experiment1.csv", "r") as csvfile:
    lines = csv.reader(csvfile)
    readlines = [i for i in lines]

num_trials = int((len(readlines[3]) - 1)/2)-2
num_points = len(readlines[3:-1])
bucket = np.zeros([num_points, num_trials])
outdoors = np.zeros_like(bucket)

for i in range(num_points):
    for j in range(num_trials):
        bucket[i][j] = readlines[3+i][1+j*2]
        outdoors[i][j] = readlines[3+i][2+j*2]

print(bucket)
print(outdoors)

# times = [i * 5 for i in range(13)]
# plt.plot(times, bucket1)
# plt.show()
