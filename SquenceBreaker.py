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

    WINDOW_SIZE = 30 #??
    variance_array = []

    # for gesture in list_of_gestures:
    #     for list_of_sensors in gesture:
    #         for columns in list_of_sensors:
    #             length = len(columns)//WINDOW_SIZE
    #             for i in range(length+1):
    #                 testdata = columns[i*WINDOW_SIZE:(i+1)*WINDOW_SIZE]
    #                 variance = np.array(testdata).var()
    #                 variance_array.append(variance)
    #             # print(len(variance_array))
            
    # for i,value in enumerate(variance_array):
    #     if value<0.001:
    #         print(i)

    # 1. chop data into window_size frame for each finger. data of 5 fingers will be in the same list.
    # 2. calculate the variance. 6 variance * 5 fingers = 30 variance
    # 3. chop data with the index of variance, classify
    def chop_data_into_frame_of_windowsize(self):
        a_gesture = self.list_of_gestures[0]
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
        for each_frame in frames:
            # do the calculation with np.var(axis=0?)
            return
        #LIST_OF_GESTURES = []


    def slide():
        """ 
        
        """

SequenceBreaker().calc_var()