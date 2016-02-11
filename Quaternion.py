import math

class Quaternion(object):

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
			self.w = 1

	# @property
	# def euler(self):
	# 	return 'Quat -> Not implemented'

	# @euler.setter
	def euler(self, x, y, z):
		c = math.cos
		s = math.sin
		# x = float(x)
		# y = float(y)
		# z = float(z)
		x = math.radians(x)
		y = math.radians(y)
		z = math.radians(z)
		cx = c(x/2)
		cy = c(y/2)
		cz = c(z/2)
		
		sx = s(x/2)
		sy = s(y/2)
		sz = s(z/2)

		q0 = cx*cy*cz + sx*sy*sz
		q1 = sx*cy*cz - cx*sy*sz
		q2 = cx*sy*cz + sx*cy*sz
		q3 = cx*cy*sz - sx*sy*cz
		# print 'go'
		# q0 = cx*cy*cz - sx*sy*sz
		# q1 = sx*cy*cz + cx*sy*sz
		# q2 = cx*sy*cz - sx*cy*sz
		# q3 = cx*cy*sz + sx*sy*cz
		print q0
		print q1
		print q2
		print q3
		print ' '
		a = math.degrees(2.0*math.acos(q0))
		print a
		bx = math.degrees(math.acos(q1/s(a/2)))
		by = math.degrees(math.acos(q2/s(a/2)))
		bz = math.degrees(math.acos(q3/s(a/2)))
		print bx
		print by
		print bz 
		print ' '
		print c(bx)
		print c(by)
		print c(bz)


	def __str__(self):
		return '{0}, {1}, {2}, {3}'.format(self.x, self.y, self.z, self.w)
	def __repr__(self):
		return '{0}, {1}, {2}, {3}'.format(self.x, self.y, self.z, self.w)

def euler(x, y, z):
	c = math.cos
	s = math.sin
	# x = float(x)
	# y = float(y)
	# z = float(z)
	x = math.radians(x)
	y = math.radians(y)
	z = math.radians(z)
	cx = c(x/2)
	cy = c(y/2)
	cz = c(z/2)
	
	sx = s(x/2)
	sy = s(y/2)
	sz = s(z/2)

	q0 = cx*cy*cz + sx*sy*sz
	q1 = sx*cy*cz - cx*sy*sz
	q2 = cx*sy*cz + sx*cy*sz
	q3 = cx*cy*sz - sx*sy*cz
	# print 'go'
	# q0 = cx*cy*cz - sx*sy*sz
	# q1 = sx*cy*cz + cx*sy*sz
	# q2 = cx*sy*cz - sx*cy*sz
	# q3 = cx*cy*sz + sx*sy*cz
	print q0
	print q1
	print q2
	print q3
	print ' '
	a = math.degrees(2.0*math.acos(q0))
	print a
	bx = math.degrees(math.acos(q1/s(a/2)))
	by = math.degrees(math.acos(q2/s(a/2)))
	bz = math.degrees(math.acos(q3/s(a/2)))
	print bx
	print by
	print bz 
	print ' '
	print c(bx)
	print c(by)
	print c(bz)