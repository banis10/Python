import cv2
cam = cv2.VideoCapture(0)
cv2.namedWindow("test")
while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:# ESC     
        break
    elif k%256 == 32:    # ESPACIO
        img_name = "DPI.JPG"
        cv2.imwrite(img_name, frame)

cam.release()
cv2.destroyAllWindows()