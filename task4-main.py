"""
* Team Id : 2778
* Author List : Chanakya,Dharmesh

* Filename: task4-main.py
* Theme: Planter Bot
* Functions: functions from newcode2.py,motor.py,zone_indiactor.py,control_led.py
* Global Variables: 
"""
# USAGE
# python picamera_fps_demo.py
# python picamera_fps_demo.py --display 1

# import the necessary packages

from __future__ import print_function
from imutils.video.pivideostream import PiVideoStream
from imutils.video import FPS
from picamera.array import PiRGBArray
from picamera import PiCamera
import argparse
import imutils
import time

import cv2
import newcode2
import motor
import zone_indicator
import control_led


background = cv2.imread('Plantation.png') 
cv2.imshow("Plantation",background)


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--num-frames", type=int, default=100,
	help="# of frames to loop over for FPS test")
ap.add_argument("-d", "--display", type=int, default=-1,
	help="Whether or not frames should be displayed")
args = vars(ap.parse_args())

# initialize the camera and stream
camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))
stream = camera.capture_continuous(rawCapture, format="bgr",
	use_video_port=True)

# allow the camera to warmup and start the FPS zoneer

time.sleep(0.5)
fps = FPS().start()


##########################################################
##This is only to initiate camera properly
# loop over some frames
for (i, f) in enumerate(stream):
	# grab the frame from the stream and resize it to have a maximum
	# width of 320 pixels
	frame = f.array
	frame = imutils.resize(frame, width=320)

	# check to see if the frame should be displayed to our screen
	if args["display"] > 0:
		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF

	# clear the stream in preparation for the next frame and update
	# the FPS zoneer
	rawCapture.truncate(0)
	fps.update()

	# check to see if the desired number of frames have been reached

	if i == i:
		break
########################################################
# stop the timer and display FPS information
fps.stop()


# do a bit of cleanup
cv2.destroyAllWindows()
stream.close()
rawCapture.close()
camera.close()


# created a *threaded *video stream, allow the camera sensor to warmup,
# and start the FPS zoneer
#print("[INFO] sampling THREADED frames from `picamera` module...")
vs = PiVideoStream().start()
time.sleep(0.5)
fps = FPS().start()

##############
binary_inv = False
cx = 0
cy = 0
zone = 0
delay = 0.17
Shed = False
ZI_Detected = False
#barren_land: Indicate wheather bot is in barrent_land or not
barren_land = False
###############

bgimage = cv2.imread("Plantation.png")
cv2.imshow('Plantation',bgimage)
motor.motor_setup()
try:
  while True:
    
     
   
  	# grab the frame from the threaded video stream and resize it
  	# to have a maximum width of 320 pixels
    
    frame = vs.read()
    frame = imutils.resize(frame, width=320)

        
    
  	# check to see if the frame should be displayed to our screen
    if args["display"] > 0:
      cv2.imshow("Frame", frame)
      key = cv2.waitKey(1) & 0xFF
      
    #for inverted plain
    if(zone >= 5 and area > 10000 and not barren_land):
      if Shed:
        print("Shed is Detected")
        motor.motor_forward(0.30)
        motor.motor_stop()
        #time.sleep(2)
        motor.GPIO.cleanup
        break
      #Barrier detected  
      print("Barrier land started")
      time.sleep(0.3)
      delay = 0.25
      barren_land = True
      Shed = True  
    
    #Barrier Ended
    if(barren_land):
      cx, black_area = newcode2.Process_Image(frame.copy(),not barren_land)
      if(black_area <7000):
        print("Barrier land ended")
        #time.sleep(2)
        delay = 0.17
        barren_land = False
    
    cx,area = newcode2.Process_Image(frame.copy(),barren_land)
    

      
    #print (cx,"is cx and cy")
    if area > 18000 and not ZI_Detected and zone < 5:
      print("Zone Indicator")
      ZI_Detected = True      
      delay = 0.04
      time.sleep(0.2)
      
    
    #decide of direction of motion based on difference between original centroid and detected centroid  
    if cx>=180:
      print("Turn Right ",cx-180)
      motor.motor_right(cx-180)      
     
    elif cx>=130 and cx<=180:
      print("On Track")
      motor.motor_forward(delay)        
       
    #to backtrack the bot
    elif cx < 0:
      print("I cant see anythink")
      motor.motor_reverse()
      motor.motor_blind()
    
    elif cx<=130:
      print("Turn Left ",130-cx)      
      motor.motor_left(130-cx)
      
    if ZI_Detected and (area < 10000) and  cx>=100 and cx<=200 and zone <= 5:
      zone = zone + 1
      print("End of ZI")
      time.sleep(0.2)      
      if(zone < 5):      
        motor.motor_stop()
        
        #cv2.imwrite('zi_pic.jpg',frame)                    
        zone_indicator.do_Zone_Indicator_Activity(zone,frame)
        
        ZI_Detected = False
        delay = 0.17  
        motor.motor_setup()
        
    fps.update()

  #to link at shed area all leds
  control_led.blink_All_Led()
  
 #   if(key == 'q'):
  #    break 
      
except KeyboardInterrupt :
    print("keyboard")
    motor.motor_stop()
    #GPIO.cleanup()
finally :
    print("finnaly")
    motor.motor_stop()
    motor.GPIO.cleanup()  

# stop the timer and display FPS information
fps.stop()

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
