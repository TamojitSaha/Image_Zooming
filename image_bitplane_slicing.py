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

#slc  = channel & pow(2, 1)
#plt.imsave('plane_'+str(1)+'.jpg',slc, format='jpg')
#
#slc  = channel & pow(2, 2)
#plt.imsave('plane_'+str(2)+'.jpg',slc, format='jpg')
#
#slc  = channel & pow(2, 3)
#plt.imsave('plane_'+str(3)+'.jpg',slc, format='jpg')
#
#
#slc  = channel & pow(2, 4)
#plt.imsave('plane_'+str(4)+'.jpg',slc, format='jpg')
#
#slc  = channel & pow(2, 5)
#plt.imsave('plane_'+str(5)+'.jpg',slc, format='jpg')
#
#slc  = channel & pow(2, 6)
#plt.imsave('plane_'+str(6)+'.jpg',slc, format='jpg')
#
#slc  = channel & pow(2, 7)
#plt.imsave('plane_'+str(7)+'.jpg',slc, format='jpg')
