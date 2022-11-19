import time
import sys
import cv2
import numpy as np
import smtplib
import threading
Fire_Reported = 0
video = cv2.VideoCapture("Rocket Launch - 228.mp4") # If you want to use a webcam use
Index like 0,1.
while True:
(grabbed, frame) = video.read()
if not grabbed:
break
frame = cv2.resize(frame, (850, 540))
blur = cv2.GaussianBlur(frame, (21, 21), 0)
hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
lower = [110, 50, 50] # threshold value for fire colour
upper = [130, 255, 255]
lower = np.array(lower, dtype="uint8")
upper = np.array(upper, dtype="uint8")
mask = cv2.inRange(hsv, lower, upper)
output = cv2.bitwise_and(frame, hsv, mask=mask)
no_red = cv2.countNonZero(mask)
if int(no_red) > 15000:
Fire_Reported = Fire_Reported + 1
cv2.imshow("output",output)
cv2.imshow("video",frame)
if cv2.waitKey(1) & 0xFF == ord('q'): #For killing the program
break
cv2.destroyAllWindows()
video.release()