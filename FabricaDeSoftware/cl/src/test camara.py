#%%
import cv2

#rtsp_url = "rtsp://admin:admin@192.168.4.168:554"
vcap = cv2.VideoCapture("rtsp://admin:admin@192.168.4.54:554")

while(1):

    ret, frame = vcap.read()
    cv2.imshow('VIDEO', frame)
    cv2.waitKey(1)

#%%
import sys

locate_python = sys.exec_prefix

print(locate_python)

#%%
import cv2
import numpy as np
#This code shows only 1 frame.

vcap = cv2.VideoCapture("rtsp://admin:admin@192.168.4.54:554")
while(1):
    ret, frame = vcap.read()
    cv2.imshow('VIDEO', frame)
    cv2.waitKey(0)