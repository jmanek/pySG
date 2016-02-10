from Transform import Transform
from Mesh import Mesh

class Node(object):

	def __init__(self):
		self.transform = Transform()
		self.mesh = None
		self.children = None
		self._parent = None

	@property
	def position(self): return self.transform.position

	@position.setter
	def position(self, pos):
		self.transform.setPosition(pos)

	@property
	def scale(self):
		return self.transform.scale
	
	@scale.setter
	def scale(self, pos):
		self.transform.setScale(pos)

	@property
	def rotation(self):
		return self.transform.rotation

	@rotation.setter
	def rotation(self, pos):
		self.transform.setRotation(pos)

	@property
	def parent(self):
	    return self._parent

	@parent.setter
	def parent(self, parent):
		self._parent = parent
		self.transform.parent = parent
	