# 导入cv图片
import cv2 as cv

# 读取图片
img = cv.imread('face/face3.jpg')
# 坐标
# (x,y)宽、高
x,y,w,h = 100,100,100,100
# 绘制矩形
# (图片,(横坐标,纵坐标,横坐标+宽,纵+高),color=(B,G,R),线宽度)  最大255
cv.rectangle(img,(x,y,x+w,y+h),color=(0,0,255),thickness=1)
# 绘制圆形
# (图片,圆心,半径,颜色,线宽度) 
cv.circle(img,center=(x+w,y+h),radius=100,color=(255,0,0),thickness=5)
# 显示
cv.imshow('re_img',img)

# 等待
# 键盘输入q可退出运行
while True:
    if ord('q') == cv.waitKey(0):
        break
# 释放内容
cv.destroyAllWindows()