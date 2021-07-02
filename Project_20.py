# -*- coding: utf-8 -*-
"""
Automatically detect rotation and line spacing of an image of text using
Radon transform
If image is rotated by the inverse of the output, the lines will be
horizontal (though they may be upside-down depending on the original image)
It doesn't work with black borders
"""

from __future__ import division, print_function
from skimage.transform import radon
from PIL import Image
from numpy import asarray, mean, array, blackman
import numpy
import imutils
import cv2 as cv2
from matplotlib.mlab import rms_flat
try:
    # More accurate peak finding from
    # https://gist.github.com/endolith/255291#file-parabolic-py
    from parabolic import parabolic

    def argmax(x):
        return parabolic(x, numpy.argmax(x))[0]
except ImportError:
    from numpy import argmax

class ImRotation:
    def __init__(self, image, outimage=None, getimage=False, usecv=False):
        # Load file, converting to grayscale
        self.image_input = cv2.imread(image)
        I = asarray(Image.open(image).convert('L'))
        self.image = I - mean(I)  # Demean; make the brightness extend above and below zero
        #self.image = cv2.imread(image)
        self.image_out = outimage
        self.isOutput = getimage
        
        self.angle = self.angle_detection()
        if usecv:
            self.image = self.rotate_image_cv2()
        else:
            self.image = self.rotate_image()
        
    
    def angle_detection(self):
        # Do the radon transform and display the result
        sinogram = radon(self.image)

        # Find the RMS value of each row and find "busiest" rotation,
        # where the transform is lined up perfectly with the alternating dark
        # text and white lines
        r = array([rms_flat(line) for line in sinogram.transpose()])

        '''
        @cbook.deprecated("2.2")
        def rms_flat(a):
           """
           Return the root mean square of all the elements of *a*, flattened out.
           """
           return np.sqrt(np.mean(np.abs(a) ** 2))
        '''
        rotation = int(round(90-argmax(r)))
        return rotation

    # Image rotation 
    def rotate_image(self):
        # Rotation by imutils
        rotated = imutils.rotate(self.image_input, self.angle)
        
        # Rotation by Pillow
        #rotated = Image.fromarray(self.image).rotate(self.angle)

        if self.isOutput:
            cv2.imwrite(self.image_out, rotated)
            #cv2.imshow("After rotation", rotated)
        return rotated

    # Rotation by OpenCV
    def rotate_image_cv2(self):
        img_center = tuple(numpy.array(self.image_input.shape[1::-1]) / 2)
        rot_mat = cv2.getRotationMatrix2D(img_center, self.angle, 1.0)
        rotated = cv2.warpAffine(self.image_input, rot_mat, self.image_input.shape[1::-1], flags=cv2.INTER_LINEAR)
        if self.isOutput:
            cv2.imwrite(self.image_out, rotated)
            #cv2.imshow("After rotation", rotated)
        return rotated

text_img = 'skew-linedetection.png' #skew-linedetection.png
rotated_image = None

d = ImRotation(text_img, './rotated.jpg', False, False)
if d.isOutput:
    rotated_image = cv2.imread(d.image_out)
else:
    rotated_image = d.image

print('Found angle is: ', d.angle)
cv2.imshow('Rotated image: ', rotated_image)
cv2.waitKey(0)
print('Done')
