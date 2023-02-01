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

    data = parse_data_to_file_sensor_meter('sequence_of_gestures')
    
    # first []: list of gestures
    # second []: list of sensor
    # 3rd []: list of columns
    # 4th []: list of values

    WINDOW_SIZE = 10 #??
    variance_array = []

    for gesture in data:
        for sensor in gesture:
            for column in sensor:
                length = len(column)//WINDOW_SIZE
                for i in range(length+1):
                    testdata = column[i*WINDOW_SIZE:(i+1)*WINDOW_SIZE]
                    variance = np.array(testdata).var()
                    variance_array.append(variance)
                    
                    # exit()
    


    LIST_OF_GESTURES = []


    def slide():
        """ 
        
        """