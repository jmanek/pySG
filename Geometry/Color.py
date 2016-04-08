class Color(object):

	def __init__(self, r=0.0, g=0.0, b=0.0, a=1.0):

		self.r = r
		self.g = g
		self.b = g
		self.a = a

	@property
	def r(self):
		return self._r

	@r.setter
	def r(self, val):
		self._r  = self.normalize(val)


	@property
	def g(self):
		return self._g

	@g.setter
	def g(self, val):
		self._g  = self.normalize(val)


	@property
	def b(self):
		return self._b

	@b.setter
	def b(self, val):
		self._b  = self.normalize(val)


	# Converts a 0-255 int into a 0.0f - 1.0f representation
	# Otherwise it returns val
	@staticmethod
	def normalize(val):
		if type(val) is str: val = float(val) if '.' in val else int(val)
		if type(val) is float: return val
		return float(val)/255


	@staticmethod
	def white():
		return Color(1.0, 1.0, 1.0)

	@staticmethod
	def black():
		return Color(0.0, 0.0, 0.0)

	@staticmethod
	def red():
		return Color(1.0, 0.0, 0.0)

	@staticmethod
	def green():
		return Color(0.0, 1.0, 0.0)

	@staticmethod
	def blue():
		return Color(0.0, 0.0, 1.0)

	def __str__(self):
		return 'RGBA({0}, {1}, {2}, {3})'.format(self.r, self.g, self.b, self.a)

	def __repr__(self):
		return 'RGBA({0}, {1}, {2}, {3})'.format(self.r, self.g, self.b, self.a)
