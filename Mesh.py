from Vector3 import Vector3
from Vector2 import Vector2
from Face import Face

class Mesh:

	def __init__(self):
		self.vertices = []
		self.faces = []
		self.normals = []
		self.texCoords = []

	def addVertex(self, *args):
		if len(args) == 3:
			self.vertices.append(Vector3(args[0], args[1], args[2]))
		else:
			self.vertices.append(args[0])

	def addFace(self, *args):
		if len(args) > 1:
			self.faces.append(Face(*args))
		else:
			self.faces.append(args[0])

	def addNormal(self, *args):
		if len(args) == 3:
			self.normals.append(Vector3(args[0], args[1], args[2]))
		else:
			self.normals.append(args[0])

	def addTexCoord(self, *args):
		if len(args) == 2:
			self.texCoords.append(Vector2(args[0], args[1]))
		else:
			self.texCoords.append(args[0])