import RPi.GPIO as GPIO
import time as t
import wiringpi

# GPIO.setmode(GPIO.BCM)
wiringpi.wiringPiSetupGpio()
# GPIO.setup(4, GPIO.IN)
wiringpi.pinMode(4, 1)

while True:
	t.sleep(0.5)
	print(wiringpi.digitalRead(4))



