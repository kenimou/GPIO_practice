## KY-011 - 2 coler LED 
## Reference: http://www.pibits.net/code/ky-011-two-color-led-module-raspberry-pi-example.php

## Physical Connection              ## 
## ================================ ##
##           [Light Bulb]           ## <- reference
##  - | (GND) | (RED) | (GREEN) | S ## <- pins on board
##       GND  |  20   |   21        ## <- pins on pi


# SAMPLE CODE 
# REF: https://gist.github.com/getelectronics/0d5655e369e3564d41aaef869f693202
import RPi.GPIO as GPIO
import time
   
GPIO.setmode(GPIO.BCM)
   
# Set up Pins
RED = 20
GREEN = 21
GPIO.setup(RED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(GREEN, GPIO.OUT, initial=GPIO.LOW)
   
# Main
try:
    while True:
        GPIO.output(GREEN, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(GREEN, GPIO.LOW)
        time.sleep(1)
        GPIO.output(RED, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(RED, GPIO.LOW)
        time.sleep(1)
   
except KeyboardInterrupt:
    print('Interrupted')

except Exception as e:
    # Catch any other errors 
    print(e)

finally:
    GPIO.cleanup()