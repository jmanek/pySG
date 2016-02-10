class Face:

	def __init__(self, *args):

		#Vertex indices 
		self.vA = None
		self.vB = None
		self.vC = None
		
		#Vertex normal indices 
		self.vnA = None
		self.vnB = None
		self.vnC = None

		#Texture coord indices
		self.vtA = None
		self.vtB = None
		self.vtC = None

	# def setVertices(self, vX, vY, vZ):
	# 	self.vertices = [vX, vY, vZ]

	# def setNormals(self, nX, nY, nZ):
	# 	self.normals = [nX, nY, nZ]
	
	# def setTexCoords(self, tX, tY):
	# 	self.texCoords = [tX, tY]