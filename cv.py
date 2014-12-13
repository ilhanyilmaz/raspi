import time
import picamera
import picamera.array
import cv2

images = []
noFrames = 60

with picamera.PiCamera() as camera:
    camera.resolution = (640,480)
    camera.framerate = 90
    camera.iso = 800
    time.sleep(2)
    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'
    g=camera.awb_gains
    camera.awb_mode = 'off'
    camera.awb_gains = g
    #camera.start_preview()
    with picamera.array.PiRGBArray(camera) as stream:
        #camera.capture(stream, format='bgr', resize=(640,512))
        # At this point the image is available as stream.array
        images = []
        i=0
        for foo in camera.capture_continuous(stream, format='bgr', use_video_port=True):
            image = stream.array
            #cv2.imshow('image', image.copy())
            #images.append(image.copy())
            cv2.imwrite('seq/raspi_{}.jpg'.format(i), image)
            i+=1
            stream.truncate(0)
            print i
            if i == noFrames:
                break


#for i in range(noFrames):
#    cv2.imwrite('seq/raspi_{}.jpg'.format(i), images[i])

            #if cv2.waitKey(10) != -1:
            #    cv2.destroyAllWindows()
            #    break

        #if cv2.waitKey(20) != -1:
        #    cv2.destroyAllWindows()
