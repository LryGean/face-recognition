# 导入cv图片
import cv2 as cv

# 监测函数
def face_detect_demo():
    #灰度转换
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    #加载分类器
    face_detect = cv.CascadeClassifier('cv/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml')
    # 参数含义:(图片,缩放倍数,检测次数,0,最小,最大)
    face = face_detect.detectMultiScale(gray,1.05,5,0,(10,10),(300,300))
    for x,y,w,h in face:
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
    cv.imshow('result',img)


# 读取图片
img = cv.imread('face/face10.png')
# 建立检测函数
face_detect_demo()


# 等待
while True:
    if ord('q') == cv.waitKey(0):
        break
# 释放内容
cv.destroyAllWindows()