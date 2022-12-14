import RPi.GPIO as GPIO
import time as t

import RYG_indicator

GPIO.setmode(GPIO.BCM)
t.sleep(1)

indicator = RYG_indicator(16, 20, 21)



GPIO.cleanup()

