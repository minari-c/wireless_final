import RPi.GPIO as GPIO
import Adafruit_DHT
import time

GPIO.setmode(GPIO.BCM)

sensor = Adafruit_DHT.DHT11
print(type(sensor))
pin = 4
while True :
	print('start2')
	h, t = Adafruit_DHT.read_retry(sensor, pin)
	print('start3')
	if h is not None and t is not None :
		print("Temperature = {0:0.1f}*C Humidity = {1:0.1f}%".format(t, h))
	else:
		print('Read error')
	time.sleep(0.1)

GPIO.cleanup()
