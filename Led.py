import RPi.GPIO as GPIO
import time


def blink(p_num, term):
	GPIO.output(p_num, GPIO.HIGH)
	time.sleep(term)
	GPIO.output(p_num, GPIO.LOW)

