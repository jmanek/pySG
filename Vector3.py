import numpy as np

class Vector3:

	def __init__(self, *args):
		if len(args) == 3:
			self.x = float(args[0])
			self.y = float(args[1])
			self.z = float(args[2])
		else:
			self.x = 0.0
			self.y = 0.0
			self.z = 0.0

	def array(self):
		return np.array([self.x, self.y, self.z, 1])

	def set(self, x, y, z):
			self.x = x
			self.y = y
			self.z = z
	

	def __str__(self):
		return '{0}, {1}, {2}'.format(self.x, self.y, self.z)

	def __repr__(self):
		return '{0}, {1}, {2}'.format(self.x, self.y, self.z)