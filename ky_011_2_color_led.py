from time import sleep
import RPi.GPIO as GPIO

GREEN = 12
RED = 16


GPIO.setmode(GPIO.BOARD)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)

while True:
    try:
        GPIO.output(GREEN, True)
        sleep(1)
        GPIO.output(GREEN, False)
        sleep(1)
        GPIO.output(RED, True)
        sleep(1)
        GPIO.output(RED, False)
        sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
       
