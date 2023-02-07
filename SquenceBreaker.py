""" 
By getting a sequence of gesture data, break a sequence of gestures into seperate gestures for classifying
Rule of breaking is to evaluate variance of the data inside a window
mutithreaded design could be used in the future

Arguments
---------
sequence: a sequence of mutiple gestures

Returns
-------
a list of gestures for clasification
"""
class SequenceBreaker:
    import numpy as np
    from spotting import parse_data_to_file_sensor_meter,get_data_from_file

    list_of_gestures = parse_data_to_file_sensor_meter('sequence_of_gestures')
    
    # first []: list of gestures
    # second []: list of sensor
    # 3rd []: list of columns
    # 4th []: list of values

    WINDOW_SIZE = 5 #??
    variance_array = []


    # 1. chop data into window_size frame for each finger. data of 5 fingers will be in the same list.
    # 2. calculate the variance. 6 variance * 5 fingers = 30 variance
    # 3. chop data with the index of variance, classify
    def chop_data_into_frame_of_windowsize(self):
        a_gesture = self.list_of_gestures[0] # not generic
        length = len(a_gesture[0][0])//self.WINDOW_SIZE
        result_list = []
        for i in range(length+1):
            temp_list = []
            for each_sensor in a_gesture:
                gestures_array = self.np.array(each_sensor)
                temp_list.append(gestures_array.transpose()[i*self.WINDOW_SIZE:(i+1)*self.WINDOW_SIZE])
            result_list.append(temp_list)
        return(result_list)

    def calc_var(self):
        frames = self.chop_data_into_frame_of_windowsize()

        variance_list = []
        for each_frame in frames:
            # do the calculation with np.var(axis=0?)

            total = 0
            # Adds up values of 5 sensors
            for i in range(5):
                total += self.np.var(each_frame[i],axis=0)

            # Take the average of gxyz and axyz
            variance_list.append([self.np.mean((total/5)[:3]), self.np.mean((total/5)[3:])])

        # returns a list of windows each contains the g variance and a variance
        return variance_list
        #LIST_OF_GESTURES = []

    def seperate_gestures(self):

        variance_list = self.calc_var()

        # temp number to determine breaks
        threshold = 10

        # Using the first var for tests
        var_list = [i[0] for i in variance_list]

        window_index_list = []
        temp = 0
        for vari in var_list:
            if (temp == 0 and vari > threshold):
                temp = vari
            elif (temp != 0 and vari < threshold ):
                window_index_list.append(var_list.index(vari))

        # print(window_index_list[0])
        for i in range(len(window_index_list)-1, -1, -1):
            x = window_index_list.pop()
            if (window_index_list[-1] != x-1):
                break


        new_index_list = [0]
        new_index_list.extend(e for e in window_index_list)
        new_index_list.append(len(variance_list))

        a_gesture = self.list_of_gestures[0]
        gestures_list = []
        for i,index in enumerate(new_index_list[:-1]):
            sensors_list = []
            for each_sensor in a_gesture:
                gestures_array = self.np.array(each_sensor)
                sensors_list.append(gestures_array.transpose()[new_index_list[i]:new_index_list[i+1]].transpose())
            gestures_list.append(sensors_list)

        # print((gestures_list))
        return gestures_list
    

