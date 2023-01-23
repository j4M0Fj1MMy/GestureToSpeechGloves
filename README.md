# rsp
Catch the signal of a start -> start collecting the whole sequence of gestures -> catch the signal of the end -> stop collecting -> break the sequence into seperate gestures -> classify all of them -> form a meaningful understandable sentence

Details:
The first AI : The signal is just a gesture, so we use our gesture classifier to catch the signal.
The second AI: The chunkation of gestures is done by spotting the empty space between them, in other words evaluating the variance.
The third AI: form the sentence by combining the parts

The first AI: KNN with DTW as distance calculation function
    fit all the (6D) data and label to the model
    classify by comparing to each result, take the lowest K cost result and take the label

    Problem:
        each label correspond to a 6 values vector

