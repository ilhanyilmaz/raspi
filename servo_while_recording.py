import RPi.GPIO as GPIO
import time
import picamera
import threading

class videoThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        print 'starting record'
        #time.sleep(15)        
        with picamera.PiCamera() as camera:
            #camera.resolution = (1280,720)
            camera.resolution = (640,480)
            camera.framerate = 90
            camera.start_recording('video.h264')
            camera.wait_recording(30)
            camera.stop_recording()
        print 'stopped recording'

class servoThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7,GPIO.OUT)
        p = GPIO.PWM(7,50)
        p.start(7.5)

        for i in range(20):
            p.ChangeDutyCycle(7.5)
            time.sleep(1)
            p.ChangeDutyCycle(10.0)
            time.sleep(1)
            p.ChangeDutyCycle(5)
            time.sleep(1)
            print 'again: {0}'.format(i)

        p.stop()
        GPIO.cleanup()

def main():

    st = servoThread()
    vt = videoThread()
    
    try:
        st.start()
        vt.start()

        #time.sleep(20)
        vt.join()
        st.join()

    except:
        print "Error: unable to start thread"

if __name__ == "__main__":
    main()
