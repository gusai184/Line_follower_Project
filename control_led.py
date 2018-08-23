"""
* Team Id : 2778
* Author List : Dharmesh and Dushyant
* Filename: control_led.py
* Theme: Planter Bot
* Functions: blink_led(color,count),def blink_All_Led()
* Global Variables: NONE
"""
#####################################
import RPi.GPIO as GPIO
import time
import zone_indicator

##############################
'''
* Function Name: blink_led(color,count)
* Input: color, count
* Output: NONE
* Logic: High gpio pin accroding to need
* Example Call: blink_led("Red",2)
'''

def blink_led(color,count):
    GPIO.setmode(GPIO.BOARD)

    RED = 33
    GREEN = 13

    BLUE = 15 
    GPIO.setwarnings(False)
    GPIO.setup(RED,GPIO.OUT)
    GPIO.output(RED,1)

    GPIO.setup(GREEN,GPIO.OUT)
    GPIO.output(GREEN,1)

    GPIO.setup(BLUE,GPIO.OUT)
    GPIO.output(BLUE,1)


    if color == 'Green':
       request = '101'
    elif color == 'Red':
       request = '110'
    else:
       request = '011'

    
    while (count>0):        

        GPIO.output(RED,int(request[0]))
        GPIO.output(GREEN,int(request[1]))
        GPIO.output(BLUE,int(request[2]))
        time.sleep(1)
        GPIO.output(RED,1)
        GPIO.output(GREEN,1)
        GPIO.output(BLUE,1)

        time.sleep(1)
        count -= 1

'''
* Function Name: blink_All_Led()
* Input: NONE
* Output: NONE
* Logic: USE color_count_list to blink led which has all data
* Example Call: blink_led("Red",2)
'''

def blink_All_Led():

    global color_count_list
    for  color_count in zone_indicator.color_count_list:
      color,count = color_count.split(" ")
      print color_count
      blink_led(color,int(count))
    return 
        
