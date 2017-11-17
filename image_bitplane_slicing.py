# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 13:50:35 2017

@author: Tamojit
"""
import numpy as np
from numpy import zeros,uint8,shape

from matplotlib.pyplot import imread, imsave, cm
import matplotlib.pyplot as plt

plane = 0

image_data = imread('image.tiff')
channel = image_data[:, :, 0]
plt.imsave('red.jpg',channel,format='jpg')
plt.imsave('red_gray.jpg',channel,cmap='gray',format='jpg')
for i in range(0,8,1):
    slc  = channel & pow(2, i)
    slc = slc/pow(2, plane)
    m,n = shape(slc)
    plt.imsave('plane_'+str(i)+'.jpg',slc,cmap='gray', format='jpg')
    slc = zeros(m*n)
