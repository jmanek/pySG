class Face:


	# args:
	# v1 v2 v3 vn1 vn2 vn3 vt1 vt2 vt3
	def __init__(self, *args):

		#Vertex indices 
		if len(args) >= 3: 
			self.setVertices(args[0], args[1], args[2])
		else:
			self.vA = None
			self.vB = None
			self.vC = None
		
		#Vertex normal indices 
		if len(args) >= 6: 
			self.setNormals(args[3], args[4], args[5])
		else:
			self.vnA = None
			self.vnB = None
			self.vnC = None

		#Texture coord indices
		if len(args) == 9: 
			self.setTexCoords(args[6], args[7], args[8])
		else:
			self.vtA = None
			self.vtB = None
			self.vtC = None


		

	def setVertices(self, *args):
		self.vA = args[0]
		self.vB = args[1]
		self.vC = args[2]
		# self.vertices = [vX, vY, vZ]

	def setVNormals(self, *args):
		self.vnA = args[0]
		self.vnB = args[1]
		self.vnC = args[2]
		# self.normals = [nX, nY, nZ]
	
	def setTexCoords(self, *args):
		self.vtA = args[0]
		self.vtB = args[1]
		self.vtC = args[2]
	# 	self.texCoords = [tX, tY]