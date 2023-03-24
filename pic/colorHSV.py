import cv2
import numpy as np

# 基本的导入模块

# 设置掩膜函数
def setMask(src: np.ndarray, mask: np.ndarray) -> np.ndarray:
    channels = cv2.split(src)
# 通道分离
    result = []
    for i in range(len(channels)):
        result.append(cv2.bitwise_and(channels[i], mask))
        # 各通道于掩膜进行图像和操作
    dest = cv2.merge(result)
    # 通道合并
    return dest

class ColorFilter(object):
    def __init__(self):
        self.colorRange = []
        # 这里是颜色筛选的范围
		# 存储格式为 [ ((H起始，S起始，V起始),(H结束，S结束，V结束)), ... ]

    def __call__(self, src: np.ndarray) -> np.ndarray:
        # 必要的函数注释
        finalMask = np.zeros_like(src)[:, :, 0]
        # finalMask指的是 最终合成的掩膜
        hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
        # 将图像转为HSV通道
        for each in self.colorRange:
            # 逐一获取HSV范围
	        lower, upper = each
            # HSV范围解构为 起始 和 结束
            mask = cv2.inRange(hsv, lower, upper)
            # 制作该HSV范围的掩膜
            finalMask = cv2.bitwise_or(finalMask, mask)
            # 掩膜合并 目标颜色 = 颜色1 + 颜色2 + ... + 颜色n
			# 注：inRange()不在HSV范围内的部分 数值为 0
			
        dest = setMask(src, finalMask)
        # 设置掩膜
        return dest
	
# 调用测试
if __name__ == '__main__':
    src = cv2.imread(r'xxx.png')	# 图片路径
	
    colorFilter = ColorFilter()		# 初始化ColorFilter()对象
    colorFilter.colorRange = [
		((xxx,xxx,xxx),(xxx,xxx,xxx)),	# Color A
		((xxx,xxx,xxx),(xxx,xxx,xxx))	# Color B
	]
    dest = colorFilter(src)
    cv2.imshow('dest', dest)
    cv2.waitKey(0)
