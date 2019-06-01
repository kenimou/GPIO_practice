'''
https://github.com/timwaizenegger/raspberrypi-examples/blob/master/sensor-temperature/ky028.py
'''
from time import sleep
import RPi.GPIO as GPIO
import sys, os
import spidev 

GPIO.setmode(GPIO.BCM)
INTERNAL = 1

# DIG_PIN = 23
ANA_PIN = 0 # BCM = 0, BOARD= 27

# GPIO.setup(DIG_PIN, GPIO.IN, pull_up_down = GPIO.PUD_OFF)

spi = spidev.SpiDev()
spi.open(0,0)


def readadc(adcnum):
    # read SPI data from MCP3004 chip, 4 possible adc (0 thru 3)
    if ((adcnum > 3) or (adcnum < 0)):
        return-1
    r = spi.xfer2([1,8+adcnum <<4,0])
    print(r)
    adcout = ((r[1] &3) <<8)+r[2]
    return adcout

tolerance = 0.5 # degree
value = readadc(ANA_PIN)
lasttemp = 125.315 - 0.175529 * value # formula made through Wolfram Alpha: 'linear function (0,125);(720,0);(1023,-55)', where (readvalue, temperature)
print('Temperature: %5.2f' % lasttemp)

while True:
    try:
        value = readadc(ANA_PIN)
        # digital = GPIO.input(DIG_PIN)
        temp = 125.315 - 0.175529 * value
        if ((temp > lasttemp + tolerance) or (temp < lasttemp - tolerance)):
            print('New Temperature: %5.2f '%GPIO.input(PIN))
            lassttemp = temp
        sleep(INTERNAL)
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit(0)
