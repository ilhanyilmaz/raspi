import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.framerate = 30 # ??

    camera.iso = 200
    time.sleep(2)

    #camera.shutter_speed = camera.exposure_speed
    camera.shutter_speed = 6000000
    camera.exposure_mode = 'off'

    g = camera.awb_gains
    #camera.awb_mode = 'off'
    #camera.awb_gains = g

    sleep(10)

    camera.capture('capture.jpg')
