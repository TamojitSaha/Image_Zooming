<h1 align="center"> Image Zooming </h1> <br>

## Table of Contents
- [Introduction](#introduction)
- [License](#license)


## Introduction
[![Build Platforms](https://img.shields.io/badge/build_platform-python-3776ab.svg)](https://www.visualstudio.com/vs/)
[![Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg)](#contributors)
[![Dependent library](https://img.shields.io/badge/dependent_library-mpl__toolkits-ff7f0e.svg)](https://matplotlib.org/mpl_toolkits/index.html)

A python script for viewing pixel information of a particular selected region in an image. It can used in object tracking where the object has multiple colour present. Its application also lies in detection of counterfiet logo or lables used in various products.
<br><br>
**Code snippet**
```python
axins = zoomed_inset_axes(ax1, 9, loc=1) # zoom = 6
axins = plt.axes([1, 1, 1, 1])
axins.imshow(img, extent = [5,500,250,785],origin="upper",aspect='auto',interpolation="none")

```
```zoomed_inset_axes()``` can be used when you want the inset represents the zoom-up of the small portion in the parent axes. And ```mpl_toolkits/axes_grid/inset_locator``` provides a helper function ```mark_inset()``` to mark the location of the area represented by the inset axes


<p align="center"> 
<h3>Input Image</h3>
<img src ="https://raw.githubusercontent.com/TamojitSaha/Image_Zooming/master/image.png" width="280" height="280">
</p><br>


<p align="center">
<h3>Output Image</h3>
<img src ="https://raw.githubusercontent.com/TamojitSaha/Image_Zooming/master/pixelated.png" width="280" height="280">
</p>



## License
Contents of this repository are realeased under [CC-BY-NC-SA 4.0](./LICENSE.md) <br>
[![License: CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
