# 导入cv图片
import cv2 as cv

# 读取图片
img = cv.imread('face/face3.jpg')
# 显示原图
resize_img = cv.resize(img,dsize=(200,200))
# 显示修改后的
cv.imshow('img',img)
# 显示修改后的
cv.imshow('resize_img',resize_img)

# 打印出的参数：(高，宽，RGB通道数)
# 打印原图尺寸大小
print('未修改：',img.shape)
# 打印修改后的大小
print('修改后：',resize_img.shape)


# 等待
# 键盘输入q可退出运行
while True:
    if ord('q') == cv.waitKey(0):
        break
# 释放内容
cv.destroyAllWindows()