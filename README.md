# GestureToSpeechGloves

# Introduction
Communication plays an important role in society, however, communicating with the 
hearing-impaired community could be hard because people seldom have exposure to sign 
language. With the help of machine learning techniques, much work had been done on 
classifying sign language with cameras. Nevertheless, it is not always good to use a camera in 
public as it could cause privacy issues. Therefore, this project will solely rely on motion 
sensors.
Thanks to the rapid development of sensors, microprocessors, and mobile apps, it becomes 
easier and easier to convert sign language to speech by utilizing IMU. However, not only do
most IMU systems only consider a single gesture at a time, but they are also not mutable once 
deployed. This will be a great obstacle in communicating because people need to do a 
sentence of gestures instead of one gesture at one time in daily life. Therefore, this project 
will work on classifying a sequence of gestures from IMU devices, with a proposed extensible
system that could be managed with an application

# Objectives
By converting hand languages into speech with gyroscopes, accelerometers, and a 
microprocessor, we hope to enhance the connection between the hearing-impaired community 
and general society. Some major milestones and challenges are listed to show the procedures 
to achieve our goal.
## 1. Build a responsive data preprocessing channel that could first continuously alleviate 
input errors from 5 gyroscopes and accelerometers. Then send the obtained processed data 
from Raspberry Pi to mobile phone.
## 2. Train a supervised ML model to classify the text to speak accurately, which can handle 
different speeds of performing hand gestures and different hand shapes.
## 3. Develop a mobile application to pair with the glove as a control center with functions 
including speaking the words or sentences classified, modifying the settings of the test-tospeech function, and storing the history of past recognitions.
