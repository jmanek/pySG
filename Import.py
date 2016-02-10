import pySG

class Import(object):

	@staticmethod
	def obj(fp):
		
		node = pySG.Node()
		node.mesh = pySG.Mesh()

		with open(fp) as f:
			for line in f:
				if '#' in line: continue
				line = line.rstrip()
				if 'v ' in line:
					line = line.replace('v ', '').lstrip().split(' ')
					print line
					node.mesh.addVertex(line[0], line[1], line[2])
				elif 'vn ' in line:
					line = line.replace('vn ', '').lstrip().split(' ')
					node.mesh.addNormal(line[0], line[1], line[2])
				elif 'vt ' in line:
					line = line.replace('vt ', '').lstrip().split(' ')
					node.mesh.addTexCoord(line[0], line[1])
				elif 'f ' in line:
					line = line.replace('f ', '').lstrip().split(' ')
					face = pySG.Face()
					# f v//vn 
					if '//' in line[0]:
						line = [int(i) for l in line for i in l.split('//')]
						face.vA = line[0]
						face.vB = line[2]
						face.vC = line[4]
						face.vnA = line[1]
						face.vnB = line[3]
						face.vnC = line[5]
					# f v/vt
					elif line[0].count('/') == 1:
						line = [int(i) for l in line for i in l.split('/')]
						face.vA = line[0]
						face.vB = line[2]
						face.vC = line[4]
						face.vtA = line[1]
						face.vtB = line[3]
						face.vtC = line[5]
					# f v/vt/vn
					elif line[0].count('/') == 2:
						line = [int(i) for l in line for i in l.split('/')]
						face.vA = line[0]
						face.vB = line[3]
						face.vC = line[6]
						face.vtA = line[1]
						face.vtB = line[4]
						face.vtC = line[7]
						face.vnA = line[2]
						face.vnB = line[5]
						face.vnC = line[8]
					# f v
					else:
						line = [int(i) for i in line]
						face.vA = int(line[0])
						face.vB = int(line[1])
						face.vC = int(line[2])	

					node.mesh.faces.append(face)
		return node






