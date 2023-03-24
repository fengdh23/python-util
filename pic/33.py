import cv2
import numpy as np

def get_dominant_color(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    color = ("black", "red", "green", "blue", "yellow", "magenta", "cyan")
    boundaries = [([0, 0, 0], [180, 255, 15]), # 黑色
                  ([0, 100, 100], [10, 255, 255]), # 红色
                  ([35, 100, 100], [77, 255, 255]),
                  ([110, 100, 100], [130, 255, 255]),
                  ([20, 100, 100], [30, 255, 255]),
                  ([150, 100, 100], [170, 255, 255]),
                  ([100, 100, 100], [120, 255, 255])]
    index = -1
    for (lower, upper) in boundaries:
        index =index +1
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        # 根据颜色范围识别颜色 0 不匹配;匹配是1
        mask = cv2.inRange(image, lower, upper)
        mValue =  cv2.countNonZero(mask)
        if mValue == 0:
            print("不匹配")
            continue
        else:
            print("匹配")
        output = cv2.bitwise_and(image, image, mask=mask)
        # TODO 统计识别到的颜色的比例 为什么要除以 3
        ratio = cv2.countNonZero(mask) / (image.size / 3)
        if ratio > 0.01:
            return color[index]
            # return color[boundaries.index((lower, upper))]
    return "none"

image = cv2.imread(r'C:\\Users\\fdh32\\Pictures\\full_red.png')

color = get_dominant_color(image)
print("Dominant color:", color)
