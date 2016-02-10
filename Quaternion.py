class Quaternion:

	def __init__(self, *args):
		if len(args) == 4:
			self.x = x
			self.y = y
			self.z = z
			self.w = w
		else:
			self.x = 0
			self.y = 0
			self.z = 0
			self.w = 0
	def __str__(self):
		return '{0}, {1}, {2}, {3}'.format(self.x, self.y, self.z, self.w)
	def __repr__(self):
		return '{0}, {1}, {2}, {3}'.format(self.x, self.y, self.z, self.w)