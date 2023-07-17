import pyk4a
from pyk4a import Config, PyK4A
import cv2
import numpy as np

result = cv2.VideoWriter('C:/Users/talha/Desktop/ibrahim/test.avi', 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         30, (1280, 720))


k4a = PyK4A(
       Config(
           color_resolution=pyk4a.ColorResolution.RES_720P,
           depth_mode=pyk4a.DepthMode.NFOV_UNBINNED,
           synchronized_images_only=True,
       )
   )
k4a.start()


while 1:
    capture = k4a.get_capture()
    if np.any(capture.color):
        
        cv2.imshow("k4a", capture.color[:, :, :3])
        frame = capture.color[:, :, :3]
        result.write(frame)
        
        key = cv2.waitKey(10)
        if key != -1:
            cv2.destroyAllWindows()
            break
k4a.stop()
result.release()
