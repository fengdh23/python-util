import numpy as np
import cv2

# OpenCV库读取一张灰度图像，并使用Canny算法进行边缘检测，最后将结果显示出来。
# 其中，Canny算法的两个参数分别是低阈值和高阈值，可以根据具体情况进行调整

# 读取图片 不能中文图片名
img = cv2.imread('C:\\Users\\fdh32\\Pictures\\test.png', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('./血清-实物.png', cv2.IMREAD_GRAYSCALE)
img.data()

# if img == nil
# 边缘检测 阈值越小，细节越丰富，靠猜，不停的调试。
edges1 = cv2.Canny(img, 100, 200)
edges2 = cv2.Canny(img, 64, 128)

# 显示结果
cv2.imshow('Original', img) # 原始的图片
cv2.imshow('Canny', edges1) # 识别后的图片
# cv2.imshow('compare', np.hstack(edges1,edges2)) # 识别后的图片
cv2.waitKey(0)
cv2.destroyAllWindows()
