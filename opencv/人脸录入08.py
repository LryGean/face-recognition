#导入模块
import cv2 as cv
#摄像头
cap = cv.VideoCapture('http://admin:981222@192.168.2.190:8081/') 

falg = 1
num = 1

while(cap.isOpened()): #检测是否在开启状态
    ret__flag,Vshow = cap.read() #得到每帧图像
    #窗口可自由缩放
    cv.namedWindow('Capture_Test',0)
    cv.imshow('Capture_Test',Vshow) #显示图像
    k = cv.waitKey(1) & 0xFF #按键判断 0xFF=1B
    if k == ord('s'): #保存
        cv.imwrite('save/'+str(num)+'.lena'+'.png',Vshow)
        print("Success to save"+str(num)+".jpg")
        print("-------------------------------")
        num += 1
    elif ord('q') == k: #退出
        break
# 释放摄像头
cap.release()
# 释放内存
cv.destroyAllWindows()