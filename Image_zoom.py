# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:25:31 2017

@author: Tamojit
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cbook as mplcbook
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset


lena = mplcbook.get_sample_data('image.tiff')
# the shape of the image is 512x512
img = mpimg.imread(lena)
img_ = img[::-1]
fig = plt.figure(figsize=(3.12, 3.12))

ax1 = plt.axes([0, 0, 2, 2], frameon=False)
ax1.imshow(img,interpolation="nearest" )


axins = zoomed_inset_axes(ax1, 9, loc=1) # zoom = 6
axins = plt.axes([1, 1, 1, 1])
axins.imshow(img, extent = [5,500,250,785],origin="upper",aspect='auto',interpolation="none")


x1, x2, y1, y2 = 140, 200, 355, 410
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)

plt.xticks(visible=False)
plt.yticks(visible=False)
mark_inset(ax1, axins, loc1=2, loc2=4, fc="none", ec="0.5")
