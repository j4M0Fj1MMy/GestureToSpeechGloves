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



    # first []: list of gestures
    # second []: list of sensor
    # 3rd []: list of columns
    # 4th []: list of values

    WINDOW_SIZE = 4 #??
    variance_array = []


    # 1. chop data into window_size frame for each finger. data of 5 fingers will be in the same list.
    # 2. calculate the variance. 6 variance * 5 fingers = 30 variance
    # 3. chop data with the index of variance, classify
    def chop_data_into_frame_of_windowsize(self,x):
        self.x = x
        chopped_x = []
        for i in range(x.shape[0] - self.WINDOW_SIZE):
            chopped_x.append(x[i:i+self.WINDOW_SIZE,:])
        return(chopped_x)

    def calc_var(self, chopped_x):
        

        variance_list = []
        for each_frame in chopped_x:
            # do the calculation with np.var(axis=0)
            var = self.np.var(each_frame, axis=0)
            variance_list.append(var)

        # returns a list of windows each contains the g variance and a variance
        return variance_list


    def seperate_gestures(self, var_list):
        '''Take the list of calculated variance as input, 
        sepeate the sentence of gestures into single gesture for classifying'''
        

        # threshold number to determine breaks
        threshold = 2
        for i,var in enumerate(var_list):
            print(i,self.np.sum(var))

        # find the start
        i = 0
        for var in var_list:
            if self.np.sum(var) > threshold:
                #i+=10
                break
            else:
                i+=1

        # find the end
        k=0
        for var in var_list[::-1]:
            if self.np.sum(var) > threshold:
                k+=10
                break
            else:
                k+=1
        
        break_list = []
        stopped = False
        for j,var in enumerate(var_list[i:len(var_list)-k]):
            maxvar = []
            maxvartail = []
            for jj in range(max(0,i+j-15),i+j):
                maxvar.append(self.np.sum(var_list[jj]))
            for jj in range(i+j,min(len(var_list),i+j+15)):
                maxvartail.append(self.np.sum(var_list[jj]))
            if not stopped and self.np.sum(var) < self.np.max(maxvar)/10 and self.np.sum(var) < self.np.max(maxvartail)/10:
                # if 
                print(self.np.max(maxvar)/10)
                break_list.append(i+j)
                
                # find the next starting
                stopped = True

            elif stopped and self.np.sum(var) > self.np.max(maxvar)/10 and self.np.sum(var) > self.np.max(maxvartail)/10:
                stopped = False

        brokengestures = []
        startingi = 0
        print(break_list)

        lastlen = i
        for i,bp in enumerate(break_list):

            # don't get too short ones
            if bp-lastlen > 10:
                print(bp)
                brokengestures.append(self.x[startingi:bp])
                startingi = bp+1
                lastlen = bp

        # get back the last value
        print('test here' , (len(var_list)-k)-lastlen)
        if (len(var_list)-k)-lastlen > 10:
            brokengestures.append(self.x[lastlen:])
        else:
            if len(brokengestures) > 1:
                self.np.append(brokengestures[-1],self.x[lastlen:])
            else:
                brokengestures.append(self.x[:])
        
        return brokengestures
    

