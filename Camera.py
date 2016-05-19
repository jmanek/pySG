from Math import Vector3

import numpy as np
import math

class Camera:

	near = 1.0
	far = 100.0
	verticalFOV = 45.0
	width = 1024
	height = 756

	def __init__(self, width=None, height=None):
		self.position = Vector3()
		self.target = Vector3(0.0, 0.0, 1.0)
		self.up = Vector3.up()

		self.width = width
		self.height = height
		self.aspectRatio = None

	def rotationMatrix(self):
		w = self.target.normalize()
		u = Vector3.cross(Vector3.up().normalize(), w)
		v = Vector3.cross(w, u)
		rotMat = np.matrix([[u.x, u.y, u.z, 0.0],
				  		[v.x, v.y, v.z, 0.0],   
						[w.x, w.y, w.z, 0.0 ],
						[0.0, 0.0, 0.0, 1.0]], dtype=np.float32)
		return rotMat
		
	def translationMatrix(self):
		trsMat = np.identity(4, dtype=np.float32)
		trsMat[0][3] = -self.position.x
		trsMat[1][3] = -self.position.y
		trsMat[2][3] = -self.position.z
		return trsMat


	def cameraTransform(self):
		rotMat = self.rotationMatrix()
		trsMat = self.translationMatrix()
		return rotMat * trsMat

	def viewportTransform(self):
		x = self.width
		y = self.height
		return np.array([[x/2, 0.0, 0.0, (x-1)/2],
						 [0.0, y/2, 0.0, (y-1)/2],
						 [0.0, 0.0, 1.0, 0.0],
						 [0.0, 0.0, 0.0, 1.0]])

	def perspectiveTransform(self):
		self.aspectRatio = float(self.width)/float(self.height)
		f = math.tan(math.radians(self.verticalFOV/2.0))
		zN = self.near
		zF = self.far
		return np.matrix([[1.0/(f*self.aspectRatio), 0.0, 0.0, 0.0],
						[0.0, 1.0/f, 0.0, 0.0],
						[0.0, 0.0, (-zN - zF)/(zN - zF), 2*zF*zN/(zN - zF)],
						[0.0, 0.0, 1.0, 1.0]])
