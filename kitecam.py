from picamera import PiCamera
from time import sleep
#import datetime as dt
import os

camera = PiCamera()

camera.resolution = (2592,1944)
#camera.resolution = (640,480)
#camera.resolution = (1024,748)

interval = 10 #interval between shots in seconds
captures = 60 #number of shots to take before stopping


def findPrevPic():    #finds the last picture taken and returns the index number
	
	path = "/home/pi/Kitecam/Kitepics/"
	dirs = os.listdir( path )
	if dirs == []:
		return(-1)
	else:
		lastPicNumber = int(max(dirs)[-8:-4])
		return (lastPicNumber)



startPicNumber = findPrevPic()+1


for i in range(startPicNumber,startPicNumber+captures):
    camera.capture('Kitepics/kitecam%04d.jpg'  %i)
    sleep(interval)

