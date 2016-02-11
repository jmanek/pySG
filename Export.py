
class Export(object):

	@staticmethod
	def obj(node, fp):

		vO = 0
		vnO = 0
		vtO = 0
		vs = []
		vns = []
		vts = []
		fs = []
		with open(fp, 'w+') as fl:

			for n in [node] + node.getAllChildren():

				m = n.mesh
				t = n.transform
				t.updateMatrix()
				hasNormals = False
				hasTexCoords = False

				for v in m.vertices:
					v = t.transformVector(v)
					# fl.write('v {0} {1} {2}\n'.format(v[0], v[1], v[2]))
					vs.append('v {0} {1} {2}'.format(v[0], v[1], v[2]))
				for vn in m.normals:
					vns.append('vn {0} {1} {2}'.format(vn.x, vn.y, vn.z))
				for vt in m.texCoords:
					vts.append(('vt {0} {1}'.format(vt.x, vt.y)))
				
				if len(m.normals) != 0: hasNormals = True
				if len(m.texCoords) != 0: hasTexCoords = True
				for f in m.faces:
					l = ['f ' + str(f.vA+vO), str(f.vB+vO), str(f.vC+vO)]
					# f v/vt
					if hasTexCoords:
						l[0] += '/' + str(f.vtA+vtO)
						l[1] += '/' + str(f.vtB+vtO)
						l[2] += '/' + str(f.vtC+vtO)
						# f v/vt/vn
						if hasNormals:
							l[0] += '/' + str(f.vnA+vnO)
							l[1] += '/' + str(f.vnB+vnO)
							l[2] += '/' + str(f.vnC+vnO)
					# f v//vn
					elif hasNormals:
						l[0] += '//' + str(f.vnA+vnO)
						l[1] += '//' + str(f.vnB+vnO)
						l[2] += '//' + str(f.vnC+vnO)
					fs.append(' '.join(l))
					# fl.write(' '.join(l) + '\n')
				vO += len(m.vertices)
				vnO += len(m.normals)
				vtO += len(m.texCoords)
			fl.write('\n'.join(vs)+'\n')
			fl.write('\n'.join(vns)+'\n')
			fl.write('\n'.join(vts)+'\n')
			fl.write('\n'.join(fs))

