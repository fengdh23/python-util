import cv2
import numpy as np

# 读取图像
img = cv2.imread('./test.png')

# 转换为灰度图

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 阈值处理
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# 边缘检测
edges = cv2.Canny(thresh, 50, 150, apertureSize=3)

# 膨胀操作
kernel = np.ones((3,3), np.uint8)
dilation = cv2.dilate(edges, kernel, iterations=2)

# 查找轮廓
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 绘制轮廓
cv2.drawContours(img, contours, -1, (0, 0, 255), 2)

# 显示结果
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
