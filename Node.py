from Transform import Transform


class Node(object):

	USE_LOCAL = True

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
	def scale(self, scl):
		self.transform.setScale(scl)

	@property
	def rotation(self):
		return self.transform.rotation

	@rotation.setter
	def rotation(self, rot):
		self.transform.rotation = rot

	@property
	def parent(self):
	    return self._parent

	@parent.setter
	def parent(self, parent):
		if self.USE_LOCAL:
			self._parent = parent
			self.transform.parent = parent

	def addChild(self, node):
		if self.children is None: self.children = []
		
		self.children.append(node)
		if self.USE_LOCAL: node.parent = self

	def removeChild(self, node):
		if self.children is None: return
		try:
			self.children.remove(node)
		except ValueError:
			print 'Node not child of this node'

	def getAllChildren(self, parent=False):
		# if parent:
		# 	nodes = [self]
		# else:
		# 	nodes = []

		nodes = [self] if parent else []	
		if self.children is not None:
			for child in self.children:
				nodes += child.getAllChildren(True)
		return nodes

	def getChildMeshes(self, parent=False):
		# if parent and self.mesh is not None:
		# 	meshes = [self.mesh]
		# else:
		# 	meshes = []
		meshes = [self.mesh] if parent and self.mesh is not None else []
		if self.children is not None:
			for child in self.children:
				meshes += child.getChildMeshes(True)
		return meshes

	# def getChildMeshes(self, parent=None):
	# 	if parent is None: 
	# 		self._childMeshes = []
	# 		parent = self
	# 	elif self.mesh is not None:
	# 		parent._childMeshes.append(self.mesh)
	# 	if self.children is not None:
	# 		for child in self.children:
	# 			child.getChildMeshes(parent)
	# 	if parent is self:
	# 		return self._childMeshes


	