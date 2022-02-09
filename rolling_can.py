import cv2
import numpy as np


can = cv2.VideoCapture("/Users/local/PycharmProjects/RollingCanDetection/test/RollingCanTest#2.mp4")

while can.isOpened():
    _, frame = can.read()
    blur = cv2.medianBlur(frame, 5)
    gray_scale = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(gray_scale, cv2.HOUGH_GRADIENT, 1, 20, param1=80, param2=30, minRadius=0, maxRadius=0)
    circles = np.uint16(np.around(circles))

    counter = 0

    if circles is not None:
        for i in circles[0, :]:
            # draw outer circle
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 0, 255), 5)
            # draw center of the circle
            cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 0), 5)

            counter += 1
            break

    else: print("No circles detected")


    cv2.imshow("test", frame)

    # cv2.imshow("gray_scale", gray_scale)

    #     height, width, layers = can.shape
    #     size = (width, height)
    #     img_array.append(can)
    #
    # writer = cv2.VideoWriter('tes.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
    #
    # for i in range(len(img_array)):
    #     writer.write(img_array[i])
    #
    # writer.release()
    # cv2.imshow(writer)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        # total_frames = int(can.get(cv2.CAP_PROP_FRAME_COUNT))
        # print(total_frames)
        # print(counter)
        # print(counter, "/", total_frames)
        break
        cv2.destroyAllWindows()


