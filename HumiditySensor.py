import RPi.GPIO as GPIO
import Adafruit_DHT
import time


GPIO.setmode(GPIO.BCM)

sensor = Adafruit_DHT.DHT11
pin = 4
i = 1
while True :
	h, t = Adafruit_DHT.read_retry(sensor, pin, retries=75, delay_seconds=0.001)
	if h is not None and t is not None :
		print(f"[{i}]Temperature = {t:0.1f}*C Humidity = {h:0.1f}%")
	else:
		print('Read error')
	i += 1
	time.sleep(1)

GPIO.cleanup()
