import RPi.GPIO as GPIO
import time

pin1 = 7
pin2 = 9

GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)

GPIO.output(pin1, True)
GPIO.output(pin2, True)
time.sleep(1)

GPIO.output(pin1, True)
GPIO.output(pin2, False)
time.sleep(1)

GPIO.output(pin1, False)
GPIO.output(pin2, False)
time.sleep(1)

GPIO.output(pin1, True)
GPIO.output(pin2, True)
time.sleep(1)

