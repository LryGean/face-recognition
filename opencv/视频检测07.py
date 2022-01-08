# 导入cv图片
import cv2 as cv
import time
import numpy as np

# 监测函数
def face_detect_demo(img):
    #灰度转换
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    #加载分类器
    face_detect = cv.CascadeClassifier('cv/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')
    # 参数含义:(图片,缩放倍数,检测次数,0,最小,最大)
    face = face_detect.detectMultiScale(gray,1.1,5)
    for x,y,w,h in face:
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
    #窗口可自由缩放
    cv.namedWindow('result',0)
    #cv.resizeWindow('result',600,600)
    cv.imshow('result',img)


# 读取摄像头
# 参数说明：0：默认摄像头
# cap = cv.VideoCapture(0)

# 读取机器人摄像头
# cap = cv.VideoCapture('http://192.168.2.156:8081/')

# 读取手机摄像头
cap = cv.VideoCapture('http://admin:981222@192.168.137.25:8081/')
#cap = cv.VideoCapture('http://admin:981222@10.1.40.20:8081/')

# 读取网页摄像头
# cap = cv.VideoCapture('http://ivi.bupt.edu.cn/hls/cctv1hd.m3u8')


# 读取视频
# cap = cv.VideoCapture('mp4/王顺和王冰冰.mp4')

# read:def read(self,image: Any =None) -> None
# 当self本身有视频内容的时候，有值并且返回值为true,image表示当前真的图像
# cap.read()

cap.set(cv.CAP_PROP_FRAME_WIDTH,1920)
cap.set(cv.CAP_PROP_FRAME_HEIGHT,1080)

#获取cap的视频帧（帧：每秒多少张图片）
fps = cap.get(cv.CAP_PROP_FPS)
print(fps)
#获取cap视频流的每帧大小
size = (int(cap.get(cv.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
print(size)


# 循环
while True:
    flag,frame = cap.read()
    # 如果播放不成立的时候，假设不成立
    if not flag:
        break
    face_detect_demo(frame)
    # 保持画面持续：1
    # 保持静止持续：0
    if ord('q') == cv.waitKey(1):
        break
# 释放内容
cv.destroyAllWindows()
# 释放摄像头
cap.release()