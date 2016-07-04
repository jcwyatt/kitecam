from picamera import PiCamera
from time import sleep
#import datetime as dt
import os

def findPrevPic():    #finds the last picture taken and returns the index number
	
	path = "/home/pi/Kitecam/Kitepics/"
	dirs = os.listdir( path )
	if dirs == []:
		return(-1)
	else:
		lastPicNumber = int(max(dirs)[-8:-4])
		return (lastPicNumber)

startPicNumber = findPrevPic() + 1

camera = PiCamera()
camera.resolution = (640, 480)


for i in range(startPicNumber,startPicNumber+5):
    camera.capture('Kitepics/kitecam%04d.jpg'  %i)
    sleep(10)

