# This module will recognize the starting point of gesture
# In our discussion, we use the posture(ie.look) to indicate our start
# 
# Therefore, we need to first recognize the look gesture
# Then, look for the gesture continuously
# When we spot it, we can start the sentence recording

import numpy as np
from dtw import dtw

def recognize(cost):
    # replace this with a smarter KNN thanks
    if cost[1] < 8:
        return True
    else:
        return False 


def get_data_from_file():
    # return a list of 2 data lists
    # now it is static, will be made to dynamic
    files = ['open_V_open.txt','open_close_open.txt']
    two_data_list_of_5_sensors = []
    for file in files:
        with open(file,'r') as f:
            two_data_list_of_5_sensors.append(f.read().split('\n\n'))
    return two_data_list_of_5_sensors 


def get_input_for_dtw():
    # return the full list for DTW comparision computation
    # [[[11,12,13],[1,2,3],[2,3,4]],[[1,1,3],[1,2,3],[2,3,4]]]
    two_data_list_of_5_sensors = get_data_from_file()
    # print(two_data_list_of_5_sensors)
    sensor_data_of_file = []

    for data_list_of_5_sensors in two_data_list_of_5_sensors:
        # dealing with each file
        sensor_data = []
        for sensor in data_list_of_5_sensors:
            # dealing with each sensor
            gx,gy,gz,ax,ay,az = [],[],[],[],[],[]
            col = [gx,gy,gz,ax,ay,az]
            for row in sensor.splitlines():
                # dealing with each row of each sensor
                for j,cell in enumerate(row.split(' ')):
                    # dealing with each cell of a row
                    # not finished
                    col[j].append(float(cell[3:]))
            sensor_data.append(col)
        sensor_data_of_file.append(sensor_data)
    return sensor_data_of_file

file_sensor_data = get_input_for_dtw()


manhattan_distance = lambda x, y: np.abs(x - y)
cost = []
for i1,each_sensor in enumerate(file_sensor_data[0]):
    for i2,each_column in enumerate(each_sensor):
        x = np.array(file_sensor_data[0][i1][i2]).reshape(-1,1)  
        y = np.array(file_sensor_data[1][i1][i2]).reshape(-1,1)  

        d, cost_matrix, acc_cost_matrix, path = dtw(x, y, dist=manhattan_distance)
        cost.append(d)

def flatten(l):
    return [item for sublist in l for item in sublist]

totalg = []
totala = []
for i in range(0, len(cost),6):
    totalg.append(cost[i:i+3])
    totala.append(cost[i+3:i+6])
gg = 0
for g in flatten(totalg):
    gg += g
total_a = 0
for a in flatten(totala):
    total_a += a
print(gg/15)
print(total_a/15)
print(recognize([gg/15,total_a/15]))

# At the end, we will need to do the same thing for 30 times,
# 6 times for each finger, 6 * 5 = 30
# x = sensor_data[0] # <--
# y = sensor_data[1] # <-- 


# import matplotlib.pyplot as plt
# plt.plot(x, label='x')
# plt.plot(y, label='y')
# plt.title('Our two temporal sequences')
# plt.legend()

# plt.imshow(acc_cost_matrix.T, origin='lower', cmap='gray', interpolation='nearest')
# plt.plot(path[0], path[1], 'w')
# plt.show()