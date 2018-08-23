"""
* Team Id : 2778
* Author List : Chankaya and Dharmesh
* Filename: detect_seeds.py
* Theme: Planter Bot
* Functions: findmax(a,b,c),find_Color_Shape_Count(frame),drawContoures(gray, chosed_color)
* Global Variables: NONE
"""
import picamera
import control_led
import time    
import overlay
import cv2
import numpy as np
#################################################################################################
'''
* Function Name: findmax(a,b,c)
* Input:  a, b, c
* Output: color
* Logic: gives color whose shape occuraces are more to reduce error
* Example Call: findmax(2,3,4)
'''
def findmax(a,b,c):
        if(a>=b and a>=c):
            return "Green"
        elif(b>=c and b>=a):
            return "Red"
        else:
            return "Blue"
        
###################################################################################################
###subroutine to write results to a csv
'''
* Function Name: find_Color_Shape_Count(frame)
* Input:  frame
* Output: shape,color,count
* Logic: decide color by color range and shape,count by contours
* Example Call: find_Color_Shape_Count(frame):
'''
def find_Color_Shape_Count(frame):
    
    #take image and get three R G B color area and find contour in each area
    img = cv2.GaussianBlur(frame, (5,5), 0)
    #cv2.imshow('img', img)
    
    opfilename = 'output.png'   
        
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #cv2.imshow('hsv',hsv)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    
    #Initiazation of  color ranges
    blue_lower = np.array([ 60,40,40],np.uint8)
    blue_upper = np.array([130,255,255], np.uint8)
    blue = cv2.inRange(hsv, blue_lower, blue_upper)
    #cv2.imshow('blue',blue)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
        
    red_lower = np.array([0,50,50],np.uint8)
    red_upper = np.array([10,255,255], np.uint8)
    red1 = cv2.inRange(hsv, red_lower,red_upper)

    red_lower = np.array([170,50,50],np.uint8)
    red_upper = np.array([180,255,255], np.uint8)
    red2 = cv2.inRange(hsv ,red_lower,red_upper)
    red = red1  + red2
    #cv2.imshow('red', red)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
        
    ##########making
    kernelOpen=np.ones((5,5))
    kernelClose=np.ones((25,25))
    maskOpen=cv2.morphologyEx(red,cv2.MORPH_OPEN,kernelOpen)
    maskClose_red=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)
    #cv2.imshow('redmask', maskClose_red)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
        
    green_lower = np.array([40, 100, 50])
    green_upper = np.array([70, 255, 255])
    green = cv2.inRange(hsv, green_lower, green_upper)
    #cv2.imshow('green', green)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

        
    '''
    * Function Name: drawContoures(gray, chosed_color)
    * Input:  gray, chosed_color
    * Output: count,shape
    * Logic: decide color by color range and shape,count by contours
    * Example Call: drawContoures(gray, 'Red')
    '''
    
    def drawContoures(gray, chosed_color):
                
        ret, thresh = cv2.threshold(gray, 127,255,0)
        canny = cv2.Canny(img,100,200)
        _,contours,heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)                
        cv2.drawContours(img, contours, -1, (0,244,0),3)
        cv2.imshow('thresh',thresh)
        count = 0
        shape = ""
        for i in range(0, len(contours)):
            m = len(cv2.approxPolyDP(contours[i],0.04*cv2.arcLength(contours[i],True),True))
            area = cv2.contourArea(contours[i])
            print "area is ",area
            if area <= 400:
               continue
            cv2.drawContours(img, contours, i, (0,244,0),3)
            cv2.imshow('img',img)
            print "Area ",area
            
            if m == 4  :
                count = count + 1
                print "Square"
                shape = "Square"
            elif m == 3 :
                count = count + 1
                print "Triangle"
                shape = "Triangle"
            elif area> 200:
                count = count + 1
                print "Circle"
                shape= "Circle"
        #cv2.imshow('cont', img)
        #cv2.waitKey(100)
        cv2.destroyAllWindows()
                
        print count
        return count,shape
 
    #find  and draw contours in each color area
    count_green,shape_green = drawContoures(green, "Green")
    count_red,shape_red = drawContoures(red, "Red")
    count_blue,shape_blue = drawContoures(blue, "Blue")

    color = findmax(count_green,count_red,count_blue)
    
    if(color=="Green"):
        shape = shape_green
        count = count_green
    elif(color == "Red"):
        shape = shape_red
        count = count_red
    else:
        shape = shape_blue
        count = count_blue
        
    print "Shape : ",shape
    print "Color : ",color
    print "Count : ",count
   
    return shape,color,count    
#####################################################################################################
