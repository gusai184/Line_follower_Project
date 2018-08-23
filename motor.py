"""
* Team Id : 2778
* Author List : Dushyant,Dhruv
* Filename: motor.py
* Theme: Planter Bot
* Functions: motor_setup(),motor_forward(delay),motor_reverse(),motor_right(x),motor_left(x),motor_blind(),motor_stop()
* Global Variables: Motor1A ,Motor1B ,Motor1E ,Motor2A ,Motor2B,Motor2E,left,right
"""
import cv2
import os
from picamera import PiCamera
from picamera.array import PiRGBArray
import numpy as np
from time import sleep
import time
import RPi.GPIO as GPIO

#pins of motor
Motor1A = 32
Motor1B = 35
Motor1E = 37
Motor2A = 36
Motor2B = 38
Motor2E = 40 

#left:variable to control left motor
left = 0
#right:variable to control right motor
right = 0

"""
 * Function Name: motor_setup()
* Input: none
* Output: none
* Logic: used to initialize and setup motor parameters

* Example Call: motor_setup()
"""
def motor_setup():

    global left
    global right
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT)
    GPIO.setup(Motor2A,GPIO.OUT)
    GPIO.setup(Motor2B,GPIO.OUT)
    GPIO.setup(Motor2E,GPIO.OUT)
    left = GPIO.PWM(Motor1E, 100)
    right = GPIO.PWM(Motor2E, 100)
    
    #left.start(25)
     
    left.start(0)
    right.start(0)
'''          
def motor_start():
    left.start(25)
    right.start(32)
   '''       

"""
* Function Name: motor_forward()
* Input: delay, used to determine sleepm time
* Output: none
* Logic: drive motor forward

* Example Call: motor_forward(5)
"""
def motor_forward(delay):
 
   
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)
    left.ChangeDutyCycle(25)
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
    GPIO.output(Motor2E,GPIO.HIGH)
    right.ChangeDutyCycle(26.5)
     
    sleep(delay)
    
    left.ChangeDutyCycle(0)
    right.ChangeDutyCycle(0)
   # print("Turning motor off")


"""
 * Function Name: motor_reverse()
* Input: none
* Output: none
* Logic: to drive robot in reverse

* Example Call: motor_reverse()
"""
def motor_reverse():
 
    left.start(25)
    right.start(32)
       
    print "Turning motor on"
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)
    left.ChangeDutyCycle(25)
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.HIGH)
    right.ChangeDutyCycle(32)
     
    sleep(0.1)
    left.ChangeDutyCycle(0)
    right.ChangeDutyCycle(0)
    

"""
 * Function Name: motor_right
* Input: x
* Output: prints sleep time
* Logic: to turn right.. speed/pwm of left motor>speed/pwm of right motor

* Example Call: motor_right(5)
"""
def motor_right(x):
    
    left.start(30)
    right.start(5)
    
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)
    left.ChangeDutyCycle(25)
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.HIGH)
    right.ChangeDutyCycle(5)
    
    '''if x < 40:
      y = 0.019
    else: 
      y = (x/100.0)*0.035'''
    y = 0.035
    print y
    
    sleep(y)
    left.ChangeDutyCycle(0)
    right.ChangeDutyCycle(0)
    

"""
 * Function Name: motor_left
* Input: x
* Output: prints sleep time
* Logic: to turn left.. speed/pwm of right motor>speed/pwm of left motor

* Example Call: motor_left(5)
"""
def motor_left(x):
    
    left.start(5)
    right.start(30)
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)
    left.ChangeDutyCycle(5)
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
    GPIO.output(Motor2E,GPIO.HIGH)
    right.ChangeDutyCycle(25)
    y= 0.035
    '''if x < 40:
      y = 0.019
    else: 
      y = (x/100.0)*0.035'''
    
    print y
    
    sleep(y)
    
    left.ChangeDutyCycle(0)
    right.ChangeDutyCycle(0)


"""
 * Function Name: motor_blind()
* Input: none
* Output: none
* Logic: to detect if robot goes out of path
* in the function>
* Example Call: motor_blind()
"""
def motor_blind():
    left.ChangeDutyCycle(0)
    right.ChangeDutyCycle(0)
        

"""
 * Function Name: motor_stop()
* Input: none
* Output: none
* Logic: stop the motor by turning Enable pin to 0/low
* in the function>
* Example Call: motor_stop()
"""
def motor_stop():
    
    left.stop()
    right.stop()
    print "Stopping motor"
    left.ChangeDutyCycle(0)
    right.ChangeDutyCycle(0)
    GPIO.output(Motor1E,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.LOW)




'''
try:
  motor_setup()
  motor_forward(1)
except KeyboardInterrupt :
    print "keyboard"
    motor_stop()
    #GPIO.cleanup()
finally :
    print "finnaly"
    motor_stop()
    GPIO.cleanup()
        

count = 0
try:
  motor_setup()
      
  while(count <5 ):
    motor_forward()
    count = count + 1      
    print count
  motor_stop()
except KeyboardInterrupt :
    print "keyboard"
    motor_stop()
    #GPIO.cleanup()
finally :
    print "finnaly"
    motor_stop()
    GPIO.cleanup()
        
'''