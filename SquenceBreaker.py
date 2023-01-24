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

    WINDOW_SIZE = 10 #??
    LIST_OF_GESTURES = []

    def slide():
        """ 
        
        """