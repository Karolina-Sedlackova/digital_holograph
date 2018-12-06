import numpy as np
import cv2 as cv2
from pyueye import ueye

h_cam=ueye.HIDS(0)
ret=ueye.is_InitCamera(h_cam, None)

if ret != ueye.IS_SUCCESS:
    pass
# def cameraAssistant():
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_EXPOSURE, 5)
# # fourcc =cv.VideoWriter_fourcc(*'XVID')
# out = cv.VideoWriter('capturedvid.avi',fourcc, 20.0, (640,480))
#
# out = cv2.VideoWriter('output.avi', -1, 20.0, (640,480))
#
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        # out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
# out.release()
cv2.destroyAllWindows()

# while(True):
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#
#     # Our operations on the frame come here
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     # Display the resulting frame
#     cv2.imshow('frame',gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()