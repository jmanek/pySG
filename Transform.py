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
		self._matrix = None
		self.parent = None

	#http://run.usc.edu/cs520-s15/assign2/p245-shoemake.pdf
	# def setRotation(self, quat):
	# 	self.quat = quat
		
	# 	self.locRotMat = np.matrix([ [ 1-2*(y**2)-2*(z**2), 2*x*y+2*w*z, 2*x*z-2*w*y, 0 ],
	# 								[ 2*x*y-2*w*z, 1-2*(x**2)-2*(z**2), 2*y*z+2*w*x, 0 ],
	# 								[ 2*x*z+2*w*y, 2*y*z-2*w*x, 1-2*(x**2)-2*(y**2), 0 ],
	# 								[ 0, 0, 0, 1 ]])
	# 	self.updateMatrix()
	
	# def setPosition(self, pos):
	# 	self.position = pos
	# 	self.locTransMat = np.matrix([ [ 1, 0, 0, pos.x ],
	# 								  [ 0, 1, 0, pos.y ],
	# 							   	  [ 0, 0, 1, pos.z ],
	# 								  [ 0, 0, 0, 1 ]])
	# 	self.updateMatrix()
		
		
	# def setScale(self, vec):
	# 	self.scale = vec
	# 	self.locScaleMat = np.matrix([ [ vec.x, 0, 0, 0],
	# 								  [ 0, vec.y, 0, 0],
	# 								  [ 0, 0, vec.z, 0],
	# 								  [ 0, 0, 0, 1 ]]) 
	# 	self.updateMatrix()

	def transformVector(self, vector):

		vec =  np.dot(self._matrix, vector.array()).A[0]
		return [vec[0], vec[1], vec[2]]





	def updateMatrix(self):
		x,y,z,w = self.rotation.x, self.rotation.y, self.rotation.z, self.rotation.w
		self.rotMat = np.matrix([ [ 1-2*(y**2)-2*(z**2), 2*x*y+2*w*z, 2*x*z-2*w*y, 0 ],
								[ 2*x*y-2*w*z, 1-2*(x**2)-2*(z**2), 2*y*z+2*w*x, 0 ],
								[ 2*x*z+2*w*y, 2*y*z-2*w*x, 1-2*(x**2)-2*(y**2), 0 ],
								[ 0, 0, 0, 1 ]])
	
		self.transMat = np.matrix([ [ 1, 0, 0, self.position.x ],
									  [ 0, 1, 0, self.position.y ],
								   	  [ 0, 0, 1, self.position.z ],
									  [ 0, 0, 0, 1 ]])
		self.sclMat = np.matrix([ [ self.scale.x, 0, 0, 0],
									  [ 0, self.scale.y, 0, 0],
									  [ 0, 0, self.scale.z, 0],
									  [ 0, 0, 0, 1 ]]) 

		if self.parent is not None:
			self._matrix = self.parent.transform.matrix * self.transMat * self.rotMat * self.sclMat
		else:
			self._matrix = self.transMat * self.rotMat * self.sclMat

	@property
	def matrix(self):
		self.updateMatrix()
		return self._matrix

	@matrix.setter
	def matrix(self, mat):
		self._matrix = mat
