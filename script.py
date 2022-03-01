import cv2
import numpy as np

src = cv2.imread("source/test1.jpg")

blur_img = cv2.medianBlur(src, 7)
gray_scale = cv2.cvtColor(blur_img, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gray_scale, cv2.HOUGH_GRADIENT, 1, 1000, param1=80, param2=30, minRadius=650, maxRadius=675)

circles = np.uint16(np.around(circles))

for i in circles[0, :]:
    # draw actual circle
    cv2.circle(src, (i[0], i[1]), i[2], (0, 0, 255), 5)
    # center of the circle
    cv2.circle(src, (i[0], i[1]), 2, (0, 0, 0), 5)

cv2.imshow("Results", src)

cv2.waitKey(0)
cv2.destroyAllWindows()
