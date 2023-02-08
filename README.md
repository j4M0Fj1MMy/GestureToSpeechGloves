# rsp
What the rsp does:
rsp filter data -> keep sending data to phone

What the model does:
Catch the signal of a start -> start collecting the whole sequence of gestures -> catch the signal of the end -> stop collecting -> break the sequence into seperate gestures -> classify all of them -> form a meaningful understandable sentence -> say it

What the feedback system does:
record and label new gesture -> update gesture database -> resolve conflicts

AI Details:
The first AI : The signal is just a gesture, so we use our gesture classifier to catch the signal.
The second AI: The chunkation of gestures is done by spotting the empty space between them, in other words evaluating the variance.
The third AI: form the sentence by combining the parts

The first AI: KNN with DTW as distance calculation function
    fit all the (6D) data and label to the model
    classify by comparing to each result, take the lowest K cost result and take the label

    Problem:
        each label correspond to a 6 values vector

The second AI:
    The idea is: we have to define the size of a window, then we slide the window , if the variance is low inside the window, it should be not much movement for the hands and we chop the sequence and define the gesture there. 

    Problem:
        how large should the window be? If the window is too large, the variance will always be high and we fail to notice a stop. If the window is too small, we may even chop one gesture into half gesture. Both case is not desirable, therefore instead of any hard rules, there should be a adaptive rule to notice any gap between gestures, the idea of ML comes in place here.
