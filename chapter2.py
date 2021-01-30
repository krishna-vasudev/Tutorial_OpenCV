import cv2
import numpy as np

kernel=np.ones((5,5),np.uint8)

img=cv2.imread(r"C:\Users\DEBRAJ\Desktop\plot\lena.png")

Grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
Blurimg=cv2.GaussianBlur(Grayimg,(9,9),0)
Cannyimg=cv2.Canny(img,200,250)
Dilimage=cv2.dilate(Cannyimg,kernel,iterations=1)
Erodedimg=cv2.erode(Dilimage,kernel,iterations=1)

cv2.imshow("Gray_image",Grayimg)
cv2.imshow("Blur_image",Blurimg)
cv2.imshow("Canny_image",Cannyimg)
cv2.imshow("Dilate_image",Dilimage)
cv2.imshow("Eroded_image",Erodedimg)
cv2.waitKey(0)