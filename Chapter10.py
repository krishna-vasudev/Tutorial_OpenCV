import cv2
import numpy as np
cap=cv2.VideoCapture(0, cv2.CAP_DSHOW)#captureDevice=camera
#cap=cv2.VideoCapture(r"C:\Users\DEBRAJ\PycharmProjects\open_cvtuts\SampleVideo_1280x720_2mb.mp4")
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

mycolors=[[0,81,115,179,244,255]]
colorvalues=[[0,255,255]]
mypoints=[]

def findcolor(img,mycolors,colorvalues):
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    i=0
    newpoints=[]
    for color in mycolors:
        lower = np.array(color[0:3])
        higher = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, higher)
        x,y=getcontours(mask)
        cv2.circle(imgResult,(x,y),10,colorvalues[i],cv2.FILLED)
        #cv2.imshow(f"img{i}",mask)
        if x!=0 and y!=0:
             newpoints.append([x,y,i])
        i+=1
    return newpoints


def getcontours(img):
    contours,hierachy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area=cv2.contourArea(cnt)
        if area > 0:
            #print(area)
            cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            #print(peri)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            #print(len(approx))
            objCor=len(approx)
            x,y,w,h=cv2.boundingRect(approx)
    return x+w//2,y

def drawonCanvas(mypoints,colorvalues):
    for point in mypoints:
        cv2.circle(imgResult,(point[0],point[1]),10,colorvalues[point[2]],cv2.FILLED)


while True:
    success, img=cap.read()
    imgResult=img.copy()
    newpoints=findcolor(img,mycolors,colorvalues)
    if len(newpoints)!=0:
        for NP in newpoints:
            mypoints.append(NP)
    if len(mypoints)!=0:
        drawonCanvas(mypoints, colorvalues)
    cv2.imshow("Video",imgResult)
    if cv2.waitKey(10) & 0xFF ==ord('q'):
        break