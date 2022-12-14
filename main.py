import RPi.GPIO as GPIO
import time as t

from RYGIndicator import RYGIndicator

GPIO.setmode(GPIO.BCM)

indicator = RYGIndicator(16, 20, 21)

GPIO.cleanup()

