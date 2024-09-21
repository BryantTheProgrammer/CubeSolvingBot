'''
based on: https://www.geeksforgeeks.org/how-to-capture-a-image-from-webcam-in-python/

have to have installed opencv python libraries:
    linux> sudo apt-get install python3-opencv

    I'm not sure what the equivalent windows install is
'''
import cv2 as cv
import time

#print(cv.__version__)


# initialize the camera 
# If you have multiple cameras connected with  
# current device, assign a value in cam_port  
# variable according to that
def captureCube(file1, file2):
    # these ports depend on which usb port you use, but should be one of the following [0,1,2,3]
    cam_port1 = 0
    cam_port2 = 2

    cam1 = cv.VideoCapture(cam_port1)
    #sleep for a second to let the camera adjust to lighting.
    time.sleep(1)

    result, image1 = cam1.read()
    # releasing the camera is important for the second camera to be able to capture.
    cam1.release()


    cam2 = cv.VideoCapture(cam_port2)
    time.sleep(1)

    result, image2 = cam2.read()
    cam2.release()

    print("Camera1:",result)
    print("Camera2:",result)

    cv.imwrite(file1,image1)
    cv.imwrite(file2,image2)

