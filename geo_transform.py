import cv2
import numpy as np

img = cv2.imread("source/test_l3.jpg")

# Specify input and output coordinates that is used
# to calculate the transformation matrix
input_pts = np.float32([[850, 200], [825, 815], [1682, 796], [1734, 150]])
output_pts = np.float32([[100,100], [100,3900], [2200,3900], [2200,100]])

# Compute the perspective transform M
M = cv2.getPerspectiveTransform(input_pts,output_pts)

# Apply the perspective transformation to the image
out = cv2.warpPerspective(img, M, (img.shape[1], img.shape[0]), flags=cv2.INTER_LINEAR)

# Display the transformed image
cv2.imshow('1', out)

cv2.waitKey(0)
cv2.destroyAllWindows()
