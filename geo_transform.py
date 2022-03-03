import cv2
import numpy as np

src_img = cv2.imread("source/test_l3.jpg")

input_pts = np.float32([[785, 332], [889, 762], [1792, 505], [1585, 131]])
dst_pts = np.float32([[100, 100], [100, 1180], [1321, 1180], [1321, 100]])

matrix = cv2.getPerspectiveTransform(input_pts, dst_pts)

transform = cv2.warpPerspective(src_img, matrix, (src_img.shape[1], src_img.shape[0]), flags=cv2.INTER_LINEAR)

cv2.imwrite("source/test1.jpg", transform)

blur_img = cv2.medianBlur(transform, 7)
gray_scale = cv2.cvtColor(blur_img, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gray_scale, cv2.HOUGH_GRADIENT, 1, 100, param1=80, param2=30, minRadius=620, maxRadius=640)

point_transformed = cv2.perspectiveTransform(src_img, matrix)

# Reverse transform
inv_trans = np.linalg.pinv(matrix)
round_tripped = cv2.perspectiveTransform(point_transformed, inv_trans)

# if circles is not None:
#     circles = np.uint16(np.around(circles))
#
#     for i in circles[0, :1]:
#         # draw actual circle
#         cv2.circle(transform_2, (i[0], i[1]), i[2], (0, 0, 255), 5)
#         # center of the circle
#         cv2.circle(transform_2, (i[0], i[1]), 2, (0, 0, 0), 5)


cv2.imshow("Circle Transform", round_tripped)

cv2.waitKey(0)
cv2.destroyAllWindows()
