"""
* Team Id : 2778
* Author List : Dharmesh, Chankaya
* Filename: zone_indicator.py
* Theme: Planter Bot
* Functions: def do_Zone_Indicator_Activity(zone,frame) 
* Global Variables: color_count_list
"""

import cv2
import detect_seeds
import overlay
import picamera
import control_led
import time

#color_count_list: Helped at shed to blink LED again that have blinked from nursary to shed
global color_count_list
color_count_list = []

#################################################################################################
'''
* Function Name: do_Zone_Indicator_Activity(zone,frame):
* Input: zone - if 1 : zone A
                if 2 : zone B
                if 3 : zone C
                if 4 : Zone D  
* Output: NONE
* Logic: Decide zone A, B, C , D based on zone parameter and call find_Color_Shape_Count to get shape color and count and then           call blink_led() to blinks led   
* Example Call:do_Zone_Indicator_Activity(1,frame) 
'''
def do_Zone_Indicator_Activity(zone,frame):
      

    shape,color,count = detect_seeds.find_Color_Shape_Count(frame)

    #append color and count of shape detected at each zone to globle variable color_count_list    
    if count > 0:
      color_count_list.append(color+" " +str(count))

    print shape,color,count
    color_shape = color + " " +shape

    control_led.blink_led(color,count)

    # based on zone call appropiate method
    if(zone == 1):
      overlay.overlay_Zone_A(color_shape,count)
    elif(zone == 2):
      overlay.overlay_Zone_B(color_shape,count)
    elif(zone == 3):
      overlay.overlay_Zone_C(color_shape,count)
    elif(zone == 4):
      overlay.overlay_Zone_D(color_shape,count)

    return
-