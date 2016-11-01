# -*- coding: utf-8 -*-
import numpy as np
import cv2

# 读取图像
img = cv2.imread('messi5.jpg', 0)

cv2.imshow('image', img)
# 保存图像
cv2.imwrite('messigray.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()