# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 05:41:21 2023

@author: okyere
"""

import CV2
import mediapipe as mp
import time


cap = CV2.VideoCapture(1)

while True : 
    success, img = cap.read()
    
    CV2.imshow("Image", img)
    CV2.waitKey(1)