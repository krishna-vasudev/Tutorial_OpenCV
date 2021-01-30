import cv2
import numpy as np

def empty(a):
    pass

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver




img=cv2.imread("lambo.jpg")

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",640,240)
cv2.createTrackbar("Hue min","Trackbars",0,179,empty)
cv2.createTrackbar("Hue max","Trackbars",26,179,empty)
cv2.createTrackbar("Sat min","Trackbars",70,255,empty)
cv2.createTrackbar("Sat max","Trackbars",255,255,empty)
cv2.createTrackbar("Value min","Trackbars",193,255,empty)
cv2.createTrackbar("Value max","Trackbars",255,255,empty)







#print(img.shape)
img_resize=cv2.resize(img,(590,342))
imgHSV=cv2.cvtColor(img_resize,cv2.COLOR_BGR2HSV)
while True:
    h_min=cv2.getTrackbarPos("Hue min","Trackbars")
    h_max=cv2.getTrackbarPos("Hue max","Trackbars")
    s_min=cv2.getTrackbarPos("Sat min","Trackbars")
    s_max=cv2.getTrackbarPos("Sat max","Trackbars")
    v_min=cv2.getTrackbarPos("Value min","Trackbars")
    v_max=cv2.getTrackbarPos("Value max","Trackbars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower=np.array([h_min,s_min,v_min])
    higher=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imgHSV,lower,higher)
    img_Result=cv2.bitwise_and(img_resize,img_resize,mask=mask)



    #cv2.imshow("Original",img_resize)
    #cv2.imshow("HSVIMAGE",imgHSV)
    #cv2.imshow("Mask",mask)
    #cv2.imshow("ImageResult",img_Result)

    imgStack=stackImages(0.6,([img_resize,imgHSV],[mask,img_Result]))

    cv2.imshow("Color detection",imgStack)

    cv2.waitKey(1)

#COLOR_DETECTION