import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)

cv2.line(img,(0,0),(512,512),(0,255,0),3)
cv2.rectangle(img,(0,0),(300,250),(0,0,255),3)
cv2.circle(img,(200,300),60,(0,255,255),5)
cv2.putText(img,"opencv",(200,400),cv2.FONT_ITALIC,2,(255,255,255),1)
#img[:]=0,0,255
#print(img)

cv2.imshow("Image",img)

cv2.waitKey(0)