# 导入cv图片
import cv2 as cv

# 读取图片
img = cv.imread('face/face10.png')

#灰度转换
#参数：读取的图片
#参数：更改图片颜色
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#显示灰度
cv.imshow('gray',gray_img)
#保存灰度图片
cv.imwrite('gray/gray_face10.png',gray_img)
# 显示图片
cv.imshow('read_img', img)
# 等待
cv.waitKey(0)
# 释放内容
cv.destroyAllWindows()
