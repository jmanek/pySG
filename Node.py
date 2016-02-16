from Transform import Transform


class Node(object):

	USE_LOCAL = True

	def __init__(self):
		self.transform = Transform()
		self.name = None
		self.mesh = None
		self.children = None
		self._parent = None
		self.materials = {}

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

	def setMaterial(self, face, material):
		if type(face) is int: face = self.mesh.faces[face]
		if material not in self.materials: self.materials[material] = set()
		
		for i in range(0, len(self.materials.keys())):
			faces = self.materials[i]
			if face in faces: faces.remove(face)

		self.materials[material].add(face)

	def getMaterial(self, face):
		if type(face) is int: face = self.mesh.faces[face]
		
		for mat, faces in self.materials.items():
			if face in faces: return mat

	# def getMaterial(self, idx):
	# 	material = None
	# 	if len(self.materials) == 0:
	# 		return material
	# 	for mat, rngs in self._materials.items():
	# 		for rng in rngs:
	# 			if idx >= rng[0] and idx <= rng[1]:
	# 				material = mat
	# 				break 
	# 	return material

	# def setMaterial(self, material, matRngs):
	# 	if type(matRngs) is tuple: new
	# 	new_mats = {material: [rng]}
	# 	rngA = matRngs[0]
	#  	rngB = matRngs[1]
	# 	for mat, rngs in self._materials.items():
	# 		newRngs = []
	# 		for rng in rngs:
	# 			a = rng[0]
	# 			b = rng[1]
				
	# 			# clip any materials that are in the range of the new material, or overwrite them
				
	# 			# a is within the new range, but b is greater
	# 			if a >= rngA and a <= rngB and b > rngB:
	# 				newRngs.append((rngB + 1, b))
				
	# 			# b is within the new range, but a is smaller
	# 			elif b >= rngA and b <= rngB and a < rngA:
	# 				newRngs.append((a, rngA - 1))
				
	# 			# the old range includes the new range, split it
	# 			elif a < rngA and b > rngB
	# 				newRngs.append((a, rngA - 1))		
	# 				newRngs.append((rngB + 1, b))		
				
	# 			#  other material is before or after new material's range 
	# 			elif b < rngA or a > rngB:
	# 				newRngs.append(rng)

	# 		if len(newRngs) != 0: new_mats[mat] = newRngs

	# 	self._materials = new_mats

	