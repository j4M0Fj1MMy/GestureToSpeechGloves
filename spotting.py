# This module will recognize the starting point of gesture
# In our discussion, we use the posture(ie.look) to indicate our start
# 
# Therefore, we need to first recognize the look gesture
# Then, look for the gesture continuously
# When we spot it, we can start the sentence recording

import numpy as np
from dtw import dtw

def recognize():
    
    return True 


def get_data():
    # return a list of 2 data lists
    files = ['open_V_open.txt','open_close_open2.txt']
    two_data_list_of_5_sensors = []
    for file in files:
        with open(file,'r') as f:
            two_data_list_of_5_sensors.append(f.read().split('\n\n'))
    return two_data_list_of_5_sensors 

# temp use, can change the structure
def get_input_for_dtw():
    sensor_data = []
    two_data_list_of_5_sensors = get_data() 

    for data_list_of_5_sensors in two_data_list_of_5_sensors:
        sensor_data.append([])
        for i,sensor in enumerate(data_list_of_5_sensors):
            if i<=1:
                continue
            rows = sensor.splitlines()
            for row in rows:
                cells = row.split(' ')
                # for cell in cells:
                # not finished

                sensor_data[-1].append(float(cells[5][3:]))
            break
    return sensor_data

sensor_data = get_input_for_dtw()

for i,e in enumerate(sensor_data):
    sensor_data[i] = np.array(e).reshape(-1,1)

# At the end, we will need to do the same thing for 30 times,
# 6 times for each finger, 6 * 5 = 30
x = sensor_data[0] # <--
y = sensor_data[1] # <-- 

manhattan_distance = lambda x, y: np.abs(x - y)
d, cost_matrix, acc_cost_matrix, path = dtw(x, y, dist=manhattan_distance)

print(d)

import matplotlib.pyplot as plt
plt.plot(x, label='x')
plt.plot(y, label='y')
plt.title('Our two temporal sequences')
plt.legend()

plt.imshow(acc_cost_matrix.T, origin='lower', cmap='gray', interpolation='nearest')
plt.plot(path[0], path[1], 'w')
plt.show()