import cv2
import numpy as np


test_img = cv2.imread("source/test_l3.jpg")

# All points are in format [cols, rows]
pt_A = [850, 200]
pt_B = [825, 815]
pt_C = [1682, 796]
pt_D = [1734, 150]

# Here, I have used L2 norm. You can use L1 also.
width_AD = np.sqrt(((pt_A[0] - pt_D[0]) ** 2) + ((pt_A[1] - pt_D[1]) ** 2))
width_BC = np.sqrt(((pt_B[0] - pt_C[0]) ** 2) + ((pt_B[1] - pt_C[1]) ** 2))
maxWidth = max(int(width_AD), int(width_BC))


height_AB = np.sqrt(((pt_A[0] - pt_B[0]) ** 2) + ((pt_A[1] - pt_B[1]) ** 2))
height_CD = np.sqrt(((pt_C[0] - pt_D[0]) ** 2) + ((pt_C[1] - pt_D[1]) ** 2))
maxHeight = max(int(height_AB), int(height_CD))

input_pts = np.float32([pt_A, pt_B, pt_C, pt_D])
output_pts = np.float32([[0, 0], [0, maxHeight - 1], [maxWidth - 1, maxHeight - 1], [maxWidth - 1, 0]])
M = cv2.getPerspectiveTransform(input_pts, output_pts)
out = cv2.warpPerspective(test_img, M,(maxWidth, maxHeight),flags=cv2.INTER_LINEAR)
#
# cv2.imshow("Transform", out)

# transform_mat = cv2.getPerspectiveTransform(src, dst)
# dst = cv2.warpPerspective(src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]] )

# src: input image
# M: Transformation matrix
# dsize: size of the output image
# flags: interpolation method to be used

# src: coordinates in the source image
# dst: coordinates in the output image


blur_img = cv2.medianBlur(out, 7)
gray_scale = cv2.cvtColor(blur_img, cv2.COLOR_BGR2GRAY)


circles = cv2.HoughCircles(gray_scale, cv2.HOUGH_GRADIENT, 1, 10000, param1=80, param2=30, minRadius=0, maxRadius=0)

if circles is not None:
    circles = np.uint16(np.around(circles))

    for i in circles[0, :]:
        # draw actual circle
        cv2.circle(out, (i[0], i[1]), i[2], (0, 0, 255), 5)
        # center of the circle
        cv2.circle(out, (i[0], i[1]), 2, (0, 0, 0), 5)


print("Failure to detect circles.")
cv2.imshow("C1", out)


cv2.waitKey(0)
cv2.destroyAllWindows()
