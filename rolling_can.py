import cv2
import numpy as np


can = cv2.VideoCapture("test/RollingCan2.mp4")
font = cv2.FONT_HERSHEY_SIMPLEX
total_frames = int(can.get(cv2.CAP_PROP_FRAME_COUNT))

frame_pos = 0
# determine current frame

counter = 0
# counts the frames of circle detected
while can.isOpened():
    _, frame = can.read()
    frame = cv2.resize(frame, (1280, 720))
    frame = frame[50:500, :]
    frame_pos += 1

    blur = cv2.medianBlur(frame, 11)
    gray_scale = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(gray_scale, cv2.HOUGH_GRADIENT, 1, 100, param1=80, param2=30, minRadius=75, maxRadius=85)

    cv2.putText(frame, "FRAMES OF CIRCLE DETECTED: ", (25, 50), font, 1, (255, 0, 255), 2, cv2.LINE_4)
    cv2.putText(frame, str(counter), (515, 50), font, 1, (255, 0, 255), 2, cv2.LINE_4)
    cv2.putText(frame, "/", (575, 50), font, 1, (255, 0, 255), 2, cv2.LINE_4)
    cv2.putText(frame, str(total_frames), (600, 50), font, 1, (255, 0, 255), 2, cv2.LINE_4)

    if (frame_pos > 80) & (frame_pos < 355):
        # modify detection window
        if circles is not None:
            # avoids crash when no circles are detected
            circles = np.uint16(np.around(circles))
            counter += 1

            for i in circles[0, :]:
                # draw outer circle
                cv2.circle(frame, (i[0], i[1]), i[2], (255, 0, 0), 2)
                # draw center of the circle
                cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 0), 3)

                break

    cv2.imshow("Rolling Can Detection", frame)

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

    if cv2.waitKey(1) == ord('q'):
        total_frames = int(can.get(cv2.CAP_PROP_FRAME_COUNT))
        print("TOTAL FRAMES OF CIRCLE DETECTED:", counter, "/", total_frames)

        break
        cv2.destroyAllWindows()
