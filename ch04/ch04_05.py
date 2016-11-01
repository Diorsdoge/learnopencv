# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg', 1)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]),plt.yticks([])
plt.show()