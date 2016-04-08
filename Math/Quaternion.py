import math
import numpy as np
from Vector3 import Vector3

class Quaternion(object):

	def __init__(self, *args):
		if len(args) == 4:
			self.x = float(args[0])
			self.y = float(args[1])
			self.z = float(args[2])
			self.w = float(args[3])
		else:
			self.x = 0
			self.y = 0
			self.z = 0
			self.w = 1

	def getEuler(self):
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
		return Vector3(x, y, z)

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

		# Order XYZ
		self.x = sx * cy * cz + cx * sy * sz
		self.y = cx * sy * cz - sx * cy * sz
		self.z = cx * cy * sz + sx * sy * cz
		self.w = cx * cy * cz - sx * sy * sz


		# self.w = cx*cy*cz + sx*sy*sz
		# self.x = sx*cy*cz - cx*sy*sz
		# self.y = cx*sy*cz + sx*cy*sz
		# self.z = cx*cy*sz - sx*sy*cz
		return self


	def setMatrix(self, m):
		trace = m[0][0] + m[1][1] + m[2][2]

		if trace > 0.0:
			s = 0.5 / math.sqrt(trace + 1.0)

			self.w = 0.25 / s
			self.x = (m[2][1] - m[1][2]) * s
			self.y = (m[0][2] - m[2][0]) * s
			self.z = (m[1][0] - m[0][1]) * s
		
		elif m[0][0] > m[1][1] and m[1][1] > m[2][2]:
			s = 2.0 * math.sqrt(1.0 + m[0][0] - m[1][1] - m[2][2])

			self.w = (m[2][1] - m[1][2]) / s
			self.x = 0.25 * s
			self.y = (m[0][1] + m[1][0]) / s
			self.z = (m[0][2] + m[2][0]) / s

		elif m[1][1] > m[2][2]:
			s = 2.0 * math.sqrt(1.0 + m[1][1] - m[0][0] - m[2][2])

			self.w = (m[0][2] - m[2][0]) / s
			self.x = (m[0][1] + m[1][0]) / s
			self.y = 0.25 * s
			self.z = (m[1][2] + m[2][1]) / s

		else:
			s = 2.0 * math.sqrt(1.0 + m[2][2] - m[0][0] - m[1][1])

			self.w = (m[1][0] - m[0][1]) / s
			self.x = (m[0][2] + m[2][0]) / s
			self.y = (m[1][2] + m[2][1]) / s
			self.z = 0.25 * s

		return self

	def getMatrix(self):
		x,y,z,w = self.x, self.y, self.z, self.w
		return np.array([ [ 1-2*(y**2)-2*(z**2), 2*x*y+2*w*z, 2*x*z-2*w*y, 0 ],
							[ 2*x*y-2*w*z, 1-2*(x**2)-2*(z**2), 2*y*z+2*w*x, 0 ],
							[ 2*x*z+2*w*y, 2*y*z-2*w*x, 1-2*(x**2)-2*(y**2), 0 ],
							[ 0, 0, 0, 1 ]])	

	def getAxisAngle(self):
		angle = 2 * math.acos(self.w)
		s = math.sqrt(1 - self.w * self.w)
		if s < 0.001:
			x = self.x
			y = self.y
			z = self.z
		else:
			x = self.x / s
			y = self.y / s
			z = self.z / s
		return (Vector3(x, y, z), angle)

	def setAxisAngle(self, axis, angle):
		halfAngle = angle/2
		s = math.sin(halfAngle)

		self.x = axis.x * s
		self.y = axis.y * s
		self.z = axis.z * s
		self.w = math.cos(halfAngle)

		return self

	def set(self, x, y, z, w):
		self.x = x
		self.y = y
		self.z = z
		self.w = w




	def __mul__(self, r):
		w,x,y,z = self.w, self.x, self.y, self.z

		_x = x*r.w + w*r.x + y*r.z - z*r.y 
		_y = y*r.w + w*r.y + z*r.x - x*r.z
		_z = z*r.w + w*r.z + x*r.y - y*r.x 
		_w = w*r.w - x*r.x - y*r.y - z*r.z

		return Quaternion(_x, _y, _z, _w)

	def __setitem__(self, key, val):
		if key == 0: self.w = val
		if key == 1: self.x = val
		if key == 2: self.y = val
		if key == 3: self.z = val

	def __getitem__(self, key):
		if key == 0: return self.w
		if key == 1: return self.x
		if key == 2: return self.y
		if key == 3: return self.z


	def __str__(self):
		return '{0}, {1}, {2}, {3}'.format(self.x, self.y, self.z, self.w)
	def __repr__(self):
		return '{0}, {1}, {2}, {3}'.format(self.x, self.y, self.z, self.w)

