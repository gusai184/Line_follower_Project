"""
* Team Id : 2778
* Author List : Dharmesh
* Filename: overlay.py
* Theme: Planter Bot
* Functions: transparentOverlay(src , overlay , pos=(0,0)),
              fill_Zone_A(count, overlayimage),
              fill_Zone_B(count, overlayimage),
              fill_Zone_C(count, overlayimage),
              fill_Zone_D(count, overlayimage),
              overlay_Zone_A(color_shape, count),
              overlay_Zone_B(color_shape, count),
              overlay_Zone_C(color_shape, count),
              overlay_Zone_D(color_shape, count),
              
              
              
* Global Variables: NONE
"""
import cv2
import numpy as np

import csv
bImg = cv2.imread("Plantation.png")

#take csv file and fill dictionary  
dictionary = {}
with open('Input Table.csv') as File:
    reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    reader.next()
    for row in reader:        
        key = row[0]+' '+row[1]
        dictionary[key] = row[2]

#print dictionary



#####################################################################
# function to overlay a transparent image on backround.
# Overlay transparent images at desired postion(x,y) and Scale.
"""
Funciton Name: transparentOverlay
Input: src, overlay, pos
    :param src: Input Color Background Image
    :param overlay: transparent Image (BGRA)
    :param pos:  position where the image to be blit.
Output: src
    :src: Resultant Image
Logic:
    To combile any pixel we need to combine the foreground and background image color using alpha blending
    Apply equation : Image = alpha * Foreground + (1 - alpha) * Background

Examle Call:
        result = transparentOverlay(Target_Imag,Overlay_Image,(300,220))    
"""

  
def transparentOverlay(src , overlay , pos=(0,0)):
    overlay = cv2.resize(overlay,(30,40))
    h,w,_ = overlay.shape  # Size of pngImg
    rows,cols,_ = src.shape  # Size of background Image
    y,x = pos[0],pos[1]    # Position of overlayimage
    
    #loop over all pixels and apply the blending equation
    for i in range(h):
        for j in range(w):
            if x+i >= rows or y+j >= cols:
                continue
            alpha = float(overlay[i][j][3]/255.0) # read the alpha channel 
            src[x+i][y+j] = alpha*overlay[i][j][:3]+(1-alpha)*src[x+i][y+j]
    return src

"""
Fucntion Name: fill_Zone_A
Input : count, overlayimage
        count : no of seeds
        overlayimage : image to  overlay
output : result
        image with overlay
Logic : use transparentOverlay function
Example Call: fil_Zone_A(count, overlayimage)
"""
def fill_Zone_A(count, overlayimage):
    if(count>=1):
        result = transparentOverlay(bImg,overlayimage,(300,220))
    if(count>=2):
        result = transparentOverlay(bImg,overlayimage,(360,220))
    if(count>=3):
        result = transparentOverlay(bImg,overlayimage,(440,220))
    if(count==4):
        result = transparentOverlay(bImg,overlayimage,(520,220))
    return result

"""
Fucntion Name: fill_Zone_B
same as fill_Zone_A
"""
def fill_Zone_B(count, overlayimage):
    if(count>=1):
        result = transparentOverlay(bImg,overlayimage,(160,170))
    if(count>=2):
        result = transparentOverlay(bImg,overlayimage,(120,180))
    if(count>=3):
        result = transparentOverlay(bImg,overlayimage,(150,215))
    if(count>=4):
        result = transparentOverlay(bImg,overlayimage,(90,220))
    return result


"""
Fucntion Name: fill_Zone_C
same as fill_Zone_A
"""
def fill_Zone_C(count, overlayimage):    
    if(count>=1):
        result = transparentOverlay(bImg,overlayimage,(350,140))
    if(count>=2):
        result = transparentOverlay(bImg,overlayimage,(305,160))
    if(count>=3):
        result = transparentOverlay(bImg,overlayimage,(260,140))
    if(count>=4):
        result = transparentOverlay(bImg,overlayimage,(215,160))
    return result


"""
Fucntion Name: fill_Zone_D
same as fill_Zone_A
"""
def fill_Zone_D(count, overlayimage):
    if(count>=1):
        result = transparentOverlay(bImg,overlayimage,(610,160))
    if(count>=2):
        result = transparentOverlay(bImg,overlayimage,(560,160))
    if(count>=3):
        result = transparentOverlay(bImg,overlayimage,(510,160))
    if(count>=4):
        result = transparentOverlay(bImg,overlayimage,(460,160))
    return result
#############################################################################


'''
ZONEA
Funciton Name: overlay_Zone_A(color_shape, count)
Input: color_shape, count
    :param color_shape: color and shape 
    :param count: number of occurances
    
Output: NONE
Logic:
    choose appropiate image based on color shape and overlay based on fill_Zone_A()
Examle Call:overlay_Zone_A("Red Circle", 3)
            
'''

def overlay_Zone_A(color_shape, count):
    

    overlayimage = cv2.imread(dictionary[color_shape],cv2.IMREAD_UNCHANGED)
    result = fill_Zone_A(count, overlayimage)
    cv2.imwrite('output.png',result)
    cv2.imshow("Plantation" ,result)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

'''
ZONEB
Funciton Name: overlay_Zone_B(color_shape, count)
same as overlay_Zone_A(color_shape, count)
'''

def overlay_Zone_B(color_shape, count):
    

    overlayimage = cv2.imread(dictionary[color_shape],cv2.IMREAD_UNCHANGED)
    result = fill_Zone_B(count, overlayimage)
    cv2.imwrite('output.png',result)
    cv2.imshow("Plantation" ,result)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    


'''
ZONEC
Funciton Name: overlay_Zone_C(color_shape, count)
same as overlay_Zone_A(color_shape, count)
'''
def overlay_Zone_C(color_shape, count):
    
    overlayimage = cv2.imread(dictionary[color_shape],cv2.IMREAD_UNCHANGED)
    result = fill_Zone_C(count, overlayimage)
    cv2.imwrite('output.png',result)    
    cv2.imshow("Plantation" ,result)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    
'''
ZONED
Funciton Name: overlay_Zone_B(color_shape, count)
same as overlay_Zone_A(color_shape, count)
'''
def overlay_Zone_D(color_shape, count):
    
    overlayimage = cv2.imread(dictionary[color_shape],cv2.IMREAD_UNCHANGED)
    result = fill_Zone_D(count, overlayimage)
    cv2.imwrite('output.png',result)
    cv2.imshow("Plantation" ,result)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    
