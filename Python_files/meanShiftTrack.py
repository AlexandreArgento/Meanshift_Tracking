from imutils.video import WebcamVideoStream
import time
import cv2
import dlib

from meanshifttracker import MeanShiftTracker

if __name__ == '__main__':

    print("[info] starting to read a webcam ...")
    capWebCam = WebcamVideoStream(0).start()
    time.sleep(1.0)

    # initialize dlib face detector
    frontFaceDetector = dlib.get_frontal_face_detector()

    # meanShift tracker
    meanShifTracker = None
    curWindow = None
    boolDetectFaceinfirsFrameOnly = True

    # loop over the frames obtained from the webcam
    while True:
        frame1 = capWebCam.read()
        frame = cv2.flip(frame1, 1)

        if boolDetectFaceinfirsFrameOnly:
            faceRect = frontFaceDetector(frame, 0)

            if (len(faceRect) == 0):
                continue

            bbox = faceRect[0]

            # convert dlib rect to opencv rect
            curWindow = (int(bbox.left()), int(bbox.top()), int(bbox.right() - bbox.left()),
                         int(bbox.bottom() - bbox.top()))

            # intialize the meanShift Tracker
            meanShifTracker = MeanShiftTracker(curWindow, frame)

            boolDetectFaceinfirsFrameOnly = False
            continue

        meanShifTracker.computeNewWindow(frame)

        x, y, w, h = meanShifTracker.getCurWindow()
        bkprojectImage = meanShifTracker.getBackProjectedImage(frame)
        cv2.imshow("MeanShift Face in Back Project Image", bkprojectImage)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2, cv2.LINE_AA)

        # show the frame and update the FPS counter
        cv2.imshow("MeanShift Face Tracking", frame)

        k = cv2.waitKey(10) & 0xff
        if k == 27:
            break

    # do a bit of cleanup
    cv2.destroyAllWindows()
    capWebCam.stop()
