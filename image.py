import cv2 as cv

cap = cv.VideoCapture('rtsp://admin:Admin123@192.168.8.103:554') # it can be rtsp or http stream
 
ret, frame = cap.read()

if cap.isOpened():
    _,frame = cap.read()
    cap.release() #releasing camera immediately after capturing picture
    #if _ and frame is not None:
    cv.imwrite('tst.jpg', frame)
    
    imgin = cv.imread('tst.jpg')
    cv.imshow('IMAGE',imgin)

    cv.waitKey(0)