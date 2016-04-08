import numpy as np
import math

class Vector3(object):

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

	def normalize(self):
		mag = math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)
		return Vector3(self.x/mag, self.y/mag, self.z/mag)

	@staticmethod
	def up():
		return Vector3(0.0, 1.0, 0.0)

	@staticmethod
	def cross(a, b):
		x = a.y * b.z - a.z * b.y
		y = a.z * b.x - a.x * b.z
		z = a.x * b.y - a.y * b.x
		return Vector3(x, y, z)

	def length(self):
		return math.sqrt(self.x**2 + self.y**2 + self.z**2)

	def __neg__(self):
		return Vector3(-self.x, -self.y, -self.z)

	def __add__(self, other):
		return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

	def __sub__(self, other):
		return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

	def __mul__(self, other):
		if type(other) is Vector3:
			return 'Not implemented'
		else:
			return Vector3(self.x * other, self.y * other, self.z * other)
		
			
	def __setitem__(self, key, val):
		if key == 0: self.x = val
		if key == 1: self.y = val
		if key == 2: self.z = val

	def __getitem__(self, key):
		if key == 0: return self.x
		if key == 1: return self.y
		if key == 2: return self.z

	def __str__(self):
		return '{0}, {1}, {2}'.format(self.x, self.y, self.z)

	def __repr__(self):
		return '{0}, {1}, {2}'.format(self.x, self.y, self.z)