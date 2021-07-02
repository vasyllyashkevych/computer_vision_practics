
# GrayScale Image Convertor
# https://extr3metech.wordpress.com
 
import cv2
import numpy as np
import math

image1 = cv2.imread('../../images/6.jpg')
blue1, green1, red1 = cv2.split(image1)
cv2.imshow('color_image 1',image1)

image2 = cv2.imread('../../images/7.jpg')
blue2, green2, red2 = cv2.split(image2)
cv2.imshow('color_image 2',image2)

blue = blue1
for i, row in enumerate(blue1):
    for j, cell in enumerate(row):
        blue[i][j] = max(blue2[i][j], blue1[i][j])
        #blue[i][j] = int(np.round((blue2[i][j] + blue1[i][j] ) / 2))

green = green1
for i, row in enumerate(green1):
    for j, cell in enumerate(row):
        green[i][j] = max(green2[i][j], green1[i][j])
        #green[i][j] = int(np.round((green2[i][j] + green1[i][j] ) / 2))

red = red1
for i, row in enumerate(red1):
    for j, cell in enumerate(row):
        red[i][j] = max(red2[i][j], red1[i][j])
        #red[i][j] = int(np.round((red2[i][j] + red1[i][j] ) / 2))

        
#green = int(np.round((green2 + green1 ) / 2))
#red = int(np.round((red2 + red1 ) / 2))

image = cv2.merge((blue, green, red))
cv2.imshow('Merged image',image)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_image.jpg',gray_image)
cv2.imshow('gray_image',gray_image) 
cv2.waitKey(0)                 # Waits forever for user to press any key
cv2.destroyAllWindows()        # Closes displayed windows
 
#End of Code
