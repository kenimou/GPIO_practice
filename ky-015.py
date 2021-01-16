## KY-015 Temporature and Humidity
## Reference: https://www.thegeekpub.com/wiki/sensor-wiki-ky-015-dht11-combination-temperature-and-humidity-sensor/

## Tech Specs:
## Temperature Measurement Range: 32ºF to 122ºF( 0ºC to 50ºC)
## Temperature Measurement Accuracy: ±2ºC
## Temperature Measurement Resolution: 1ºC
## Humidity Measurement Range: 20% to 90% RH
## Humidity Measurement Resolution: ±5% RH

## Physical Connection              ## 
## ================================ ##
##           [BLUE BOX]             ## <- reference
## S | (Signal) | (V+) | (GND) | -  ## <- pins on board
##        21    |  5V  |  GND       ## <- pins on pi

## Sample Code:
# pip install Adafruit_Python_DHT
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
  
DHTSensor = Adafruit_DHT.DHT11
GPIO_Pin = 21

_temp_offset = 0
_humid_offset = -48.0
  
while True:
    humid_raw, temper_raw = Adafruit_DHT.read_retry(DHTSensor, GPIO_Pin)
    humid = humid_raw + _humid_offset
    temper = temper_raw + _temp_offset
    print(f"Temperature:  {temper:0.1f}C, Humidity: {humid:0.1f}%")
    time.sleep(3)