import cv2
import numpy as np

img=cv2.imread(r"cards.jpg")
width,height=250,350

pts1=np.float32([[332,63],[462,116],[255,256],[385,309]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgoutput=cv2.warpPerspective(img,matrix,(width,height))



cv2.imshow("Image",img)
cv2.imshow("Wraped_img",imgoutput)

cv2.waitKey(0)