import cv2
import numpy as np

img=cv2.imread(r"C:\Users\DEBRAJ\Desktop\plot\lena.png")

print(img.shape)
resized_img=cv2.resize(img,(512,512))
print(resized_img.shape)
img_cropped=resized_img[100:300,100:400]
#cv2.imshow("org_image",img)
cv2.imshow("resized_image",resized_img)
cv2.imshow("cropped_image",img_cropped)

cv2.waitKey(0)