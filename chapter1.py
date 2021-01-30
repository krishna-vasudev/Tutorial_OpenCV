import cv2
#cap=cv2.VideoCapture(0, cv2.CAP_DSHOW)#captureDevice=camera
cap=cv2.VideoCapture(r"C:\Users\DEBRAJ\PycharmProjects\open_cvtuts\SampleVideo_1280x720_2mb.mp4")
#cap.set(3,640)
#cap.set(4,480)
#cap.set(10,100)

while True:
    success, img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(10) & 0xFF ==ord('q'):
        break