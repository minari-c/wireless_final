import RPi.GPIO as GPIO

from Sensor import Sensor
import Led

class RYGIndicator(Sensor):
	def __init__(self, r_pin=16, y_pin=20, g_pin=21):
		self.r_pin = r_pin
		self.y_pin = y_pin
		self.g_pin = g_pin
		super().__init__([r_pin, y_pin, g_pin], self.__class__.__name__, 'notify current status')
		GPIO.setup(self.use_pins, GPIO.OUT)
		self.sensor_info()
		self.blink(1)


	def sensor_info(self):
		super().sensor_info()

	def blink(self, term=1):
		for led in self.use_pins:
			Led.blink(led, term)

