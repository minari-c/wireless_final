class Sensor:
	def __init__(self, u_pins=list(), s_name='no name', s_use='no use'):
		self.use_pins = u_pins
		self.sensor_name = s_name
		self.sensor_use = s_use

	def sensor_info(self):
		print(f'{self.sensor_name}: {self.sensor_use}')
		print(f'use_pins: {self.use_pins}')

