from picamera import PiCamera
from time import sleep
import datetime as dt
import os

path = "/home/pi/Kitepics/"
dirs = os.listdir( path )

for file in dirs:
    print file

'''camera = PiCamera()
camera.resolution = (640, 480)



laststored = 

for i in range(laststored,):
    camera.capture('Kitepics/kitecam'+tstamp+'.jpg')
    print ('captured :' + 'kitecam'+tstamp+'.jpg')
    sleep(5)
'''
