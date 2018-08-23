"""
* Team Id : 2778
* Author List : Dharmesh
* Filename: newcode2.py
* Theme: Planter Bot
* Functions: Process_Image(frame,barren_land)
* Global Variables: NONE
"""
import numpy as np
from picamera import PiCamera
from picamera.array import PiRGBArray
from time import sleep

import cv2
import time

'''
* Function Name: Process_Image(frame,barren_land)
* Input: (frame,barren_land)
* Output: cx - centroid of path 
          area - area of biggest contour
* Logic: use contour framming In Framming take middle frame and smooth ,threshold it based on contour 
* Example Call: Process_Image(frame,False)
'''

def Process_Image(frame,barren_land):

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        return
   
    # Crop the image
    crop_img = frame[100:215, 0:320]
    
    # Convert to grayscale
    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)

    # Gaussian blur
    blur = cv2.GaussianBlur(gray,(5,5),0)

    # Color thresholding
    
    if(barren_land):
      ret,thresh = cv2.threshold(blur,120,255,cv2.THRESH_BINARY)
    else:
      ret,thresh = cv2.threshold(blur,60,255,cv2.THRESH_BINARY_INV)

    
    # Find the contours of the frame
    _,contours,hierarchy = cv2.findContours(thresh.copy(), 1, cv2.CHAIN_APPROX_NONE)
    cx = -2
    area = 0

    # Find the biggest contour (if detected)
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)

        
        if(M['m00'] == 0):
            return -2;
            
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])

        cv2.line(crop_img,(cx,0),(cx,720),(255,0,0),1)
        cv2.line(crop_img,(0,cy),(1280,cy),(255,0,0),1)
        cv2.circle(crop_img,(cx,cy),2,(255,0,0),3)
        cv2.circle(crop_img,(cx+20,cy),2,(255,0,0),3)
        cv2.circle(crop_img,(cx-20,cy),2,(255,0,0),3)
        cv2.drawContours(crop_img, contours, -1, (0,255,0), 1)
        
        print cx," ",cy
        area = cv2.contourArea(c)
        print "Contour area",area
        #cv2.imshow('frame',crop_img)    
        if(cv2.contourArea(c) < 400):
          cx = -1
          
    return cx,area
