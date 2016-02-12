import math

class Quaternion(object):

	def __init__(self, *args):
		if len(args) == 4:
			self.x = args[0]
			self.y = args[1]
			self.z = args[2]
			self.w = args[3]
		else:
			self.x = 0
			self.y = 0
			self.z = 0
			self.w = 1

	def getEuler(self):
		print self
		q0, q1, q2, q3 = self.w, self.x, self.y, self.z
		xQ = (2*(q0*q1 + q2*q3))/(1 - 2*(q1**2 + q2**2))
		xQ = min(1.0, xQ) if xQ > 0 else max(-1.0, xQ)
		yQ =  2*(q0*q2 - q3*q1)
		yQ = min(1.0, yQ) if yQ > 0 else max(-1.0, yQ)
		zQ =  (2*(q0*q3 + q1*q2))/(1 - 2*(q2**2 + q3**2))
		zQ = min(1.0, zQ) if zQ > 0 else max(-1.0, zQ)

		x = math.degrees(math.atan( xQ ))
		y = math.degrees(math.asin( yQ ))
		z = math.degrees(math.atan( zQ ))
		return [x, y, z]

	def setEuler(self, x, y, z):
		c = math.cos
		s = math.sin
		x = math.radians(x)
		y = math.radians(y)
		z = math.radians(z)
		cx = c(x/2)
		cy = c(y/2)
		cz = c(z/2)
		
		sx = s(x/2)
		sy = s(y/2)
		sz = s(z/2)

		self.w = cx*cy*cz + sx*sy*sz
		self.x = sx*cy*cz - cx*sy*sz
		self.y = cx*sy*cz + sx*cy*sz
		self.z = cx*cy*sz - sx*sy*cz

	def set(self, x, y, z, w):
		self.x = x
		self.y = y
		self.z = z
		self.w = w



	def __str__(self):
		return '{0}, {1}, {2}, {3}'.format(self.x, self.y, self.z, self.w)
	def __repr__(self):
		return '{0}, {1}, {2}, {3}'.format(self.x, self.y, self.z, self.w)

