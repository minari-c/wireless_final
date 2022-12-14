class RYGIndicator(Sensor):
	def __init__(self, r_pin=16, y_pin=20, g_pin=21):
		self.r_pin = r_pin
		self.y_pin = y_pin
		self.g_pin = g_pin
		super().__init__([r_pin, y_pin, g_pin], self.__class__.__name__, 'notify current status')
		GPIO.setup(super().use_pins, GPIO.OUT, initial=GPIO.HIGH)

	def sensor_info(self):
		super().sensor_info()

	def 