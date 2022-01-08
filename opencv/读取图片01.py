# 导入cv图片
import cv2 as cv

# 读取图片
img = cv.imread('face/face4.png')
# 显示图片
cv.imshow('read_img', img)
# 等待
cv.waitKey(0)
# 释放内容
cv.destroyAllWindows()
