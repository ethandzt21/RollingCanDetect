import cv2
import numpy as np

test_img = cv2.imread('test/test_easy2.jpg')
test_img = cv2.resize(test_img, (0, 0), fx=1.5, fy=1.5)

gray_scale = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
blur_img = cv2.medianBlur(gray_scale, 5)

# hough circles parameter set
circles = cv2.HoughCircles(blur_img, cv2.HOUGH_GRADIENT, 1, 100, param1=80, param2=30, minRadius=0, maxRadius=0)
circles = np.uint16(np.around(circles))

for i in circles[0, :]:
    # draw actual circle
    cv2.circle(test_img, (i[0], i[1]), i[2], (0, 0, 255), 5)
    # center of the circle
    cv2.circle(test_img, (i[0], i[1]), 2, (0, 0, 0), 5)


cv2.imshow("Center of The Circle", test_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
