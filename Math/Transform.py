from Vector3 import Vector3
from Quaternion import Quaternion


import numpy as np

class Transform(object):

	def __init__(self):
		identity = np.identity(4)
		self.rotMat = identity
		self.transMat = identity
		self.scaleMat = identity
		self.position = Vector3()
		self.scale = Vector3(1, 1, 1)
		self.rotation = Quaternion()
		self._matrix = identity
		self.parent = None

	# http://run.usc.edu/cs520-s15/assign2/p245-shoemake.pdf
	def setRotation(self, quat):
		self.quat = quat
		
		self.locRotMat = np.matrix([ [ 1-2*(y**2)-2*(z**2), 2*x*y+2*w*z, 2*x*z-2*w*y, 0 ],
									[ 2*x*y-2*w*z, 1-2*(x**2)-2*(z**2), 2*y*z+2*w*x, 0 ],
									[ 2*x*z+2*w*y, 2*y*z-2*w*x, 1-2*(x**2)-2*(y**2), 0 ],
									[ 0, 0, 0, 1 ]])
		self.updateMatrix()
	
	def setPosition(self, pos):
		self.position = pos
		self.locTransMat = np.matrix([ [ 1, 0, 0, pos.x ],
									  [ 0, 1, 0, pos.y ],
								   	  [ 0, 0, 1, pos.z ],
									  [ 0, 0, 0, 1 ]])
		self.updateMatrix()
		
		
	def setScale(self, vec):
		self.scale = vec
		self.locScaleMat = np.matrix([ [ vec.x, 0, 0, 0],
									  [ 0, vec.y, 0, 0],
									  [ 0, 0, vec.z, 0],
									  [ 0, 0, 0, 1 ]]) 
		self.updateMatrix()

	def transformVector(self, vector):
		vec =  np.dot(self._matrix, vector.array())
		# print self._matrix
		# print vector.array()
		# print vec
		return Vector3(vec[0], vec[1], vec[2])

	def updateRotationMatrix(self):
		x,y,z,w = self.rotation.x, self.rotation.y, self.rotation.z, self.rotation.w
		self.rotMat = np.array([ [ 1-2*(y**2)-2*(z**2), 2*x*y+2*w*z, 2*x*z-2*w*y, 0 ],
							     [ 2*x*y-2*w*z, 1-2*(x**2)-2*(z**2), 2*y*z+2*w*x, 0 ],
							     [ 2*x*z+2*w*y, 2*y*z-2*w*x, 1-2*(x**2)-2*(y**2), 0 ],
							     [ 0, 0, 0, 1 ]])	

	def updateTranslationMatrix(self):
		self.transMat = np.array([ [ 1, 0, 0, self.position.x ],
									  [ 0, 1, 0, self.position.y ],
								   	  [ 0, 0, 1, self.position.z ],
									  [ 0, 0, 0, 1 ]])
	def updateScaleMatrix(self):
		self.sclMat = np.array([ [ self.scale.x, 0, 0, 0],
									  [ 0, self.scale.y, 0, 0],
									  [ 0, 0, self.scale.z, 0],
									  [ 0, 0, 0, 1 ]]) 
	
	def decompose(self, m):
		self._matrix = m
		# scaleX = Vector3(m[0][0], m[1][0], m[2][0]).length()
		# scaleY = Vector3(m[0][1], m[1][1], m[2][1]).length()
		# scaleZ = Vector3(m[0][2], m[1][2], m[2][2]).length()
		# if np.linalg.det(m) < 0.0: scaleX = -scaleX

		# m[0][0] /= scaleX
		# m[1][0] /= scaleX
		# m[2][0] /= scaleX

		# m[0][1] /= scaleY
		# m[1][1] /= scaleY
		# m[2][1] /= scaleY

		# m[0][2] /= scaleZ
		# m[1][2] /= scaleZ
		# m[2][2] /= scaleZ

		# self.position.set(m[0][3], m[1][3], m[2][3])
		# self.rotation.setMatrix(m)
		# self.scale.set(scaleX, scaleY, scaleZ)


	def updateMatrix(self):
		self.updateRotationMatrix()
		self.updateTranslationMatrix()
		self.updateScaleMatrix()

		if self.parent is not None:
			self._matrix = np.dot(self.parent.transform.matrix, np.dot(self.transMat, np.dot(self.rotMat, self.sclMat)))
		else:
			self._matrix = np.dot(self.transMat, np.dot(self.rotMat, self.sclMat))

	def rotate(self, *args):
		if len(args) == 1:
			rot = args[0]
		elif len(args) == 3:
			rot = Quaternion().setEuler(args[0], args[1], args[2])
		elif len(args) == 4:
			rot = Quaternion(args[0], args[1], args[2], args[3])
		
		self.rotation = rot * self.rotation

	@property
	def matrix(self):
		# self.updateMatrix()
		return self._matrix

	@matrix.setter
	def matrix(self, mat):
		self._matrix = mat
