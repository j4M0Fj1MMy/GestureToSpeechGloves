# This module will recognize the starting point of gesture
# In our discussion, we use the posture(ie.look) to indicate our start
# 
# Therefore, we need to first recognize the look gesture
# Then, look for the gesture continuously
# When we spot it, we can start the sentence recording

import numpy as np
import AnotherDtw as knndtw

def get_data_from_file(folder):
    # return a list of 2 data lists
    # now it is static, will be made to dynamic
    import os

    files = [file for file in os.listdir(folder)]
    # files = ['open_V_open.txt','open_close_open.txt']
    all_data_from_files = []
    for file in files:
        with open(f'{folder}/'+file,'r') as f:
            all_data_from_files.append(f.read().split('\n\n'))
    return all_data_from_files 

def flatten(l):
    return [item for sublist in l for item in sublist]

def parse_data_to_file_sensor_meter(folder):
    #Probem with old way, the data is dumped once it is DTWed, we need to store all the data into memory for predict()

    # return the full list for DTW comparision computation
    # [[[11,12,13],[1,2,3],[2,3,4]],[[1,1,3],[1,2,3],[2,3,4]]]
    all_data_from_files = get_data_from_file(folder)
    # print(two_data_list_of_5_sensors)
    sensor_data_of_files = []

    for data_list_of_5_sensors in all_data_from_files:
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
                    col[j].append(float(cell[3:]))
            sensor_data.append(col)
        sensor_data_of_files.append(sensor_data)
    return sensor_data_of_files

def main(gestures):
    data = parse_data_to_file_sensor_meter('gestures')
    # the data is formatted as file_list -> sensor_list -> meter_list
    # By column, I mean column of sensor i.e. meter
    # By file, each file contain a gesture
    import time
    tempLabel = np.array(['borrow','borrow','borrow','oco','oco','oco','ovo','ovo','ovo','p','p','tshirt','tshirt','tshirt','try','try','try'])

    model = knndtw.KnnDtw(n_neighbors=3)
    model.fit(data,tempLabel)

    start_time = time.time()
    result = model.predict(gestures)
    print(result[0],result[1])

    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    from SquenceBreaker import SequenceBreaker
    gestures = SequenceBreaker().seperate_gestures()
    SequenceBreaker().plotgraph()
    # gestures = [parse_data_to_file_sensor_meter('gestures')[2]]
    main(gestures)