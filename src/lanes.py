'''
Created on Nov 25, 2019

@author: licaretim
'''
import cv2
import os
import numpy as np

image_path=os.path.join(os.path.realpath('..'),'test_image.jpg')
image = cv2.imread(image_path) # load image into a multi-dimensional array (RGB) 
cv2.imshow('results', image) # print image
# cv2.waitKey(0)  # keep the image on display until user input
# lane_image = np.copy(image) # does NOT reflect changes from np array in the original image

def canny(image):
   # convert image to grayscale - turn image from 3 channels to 1 channel (for faster processing)
   gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
#    cv2.imshow('results', gray)
#    cv2.waitKey(0)   
   # apply Gaussian blur to reduce noise and smoothen image to improve edge detection
   # option 1: average pixel value based on the values (weighted avg = kernel) of surrounding pixels
   blur=cv2.GaussianBlur(gray, (5,5), 0) # apply a 5,5 kernel gaussian blur with a deviation of 0
#    cv2.imshow('results', blur)
#    cv2.waitKey(0)   
   # apply the Canny function to detect edges - 
   # calculates a derivative on f(x,y), where f is the pixel intensity, 
   # x and y are matrix (image) pixel coordinates
   # the derivative of f is the gradient -> low value of f' = low gradient = low diff in pixel intesity 
   # high value of f' = high gradient = high difference in pixel intesity
   canny = cv2.Canny(blur, 50, 150)
#    cv2.imshow('results', canny)  # gradient image
#    cv2.waitKey(0)
   return canny
 
# specifying the region of interesting_normal

canny = canny(lane_image)
cv2.imshow('results', canny)  # gradient image
cv2.waitKey(0)