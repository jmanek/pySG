
class Export(object):

	@staticmethod
	def obj(node, fp):
		m = node.mesh
		t = node.transform
		hasNormals = False
		hasTexCoords = False
		with open(fp, 'w+') as fl:
			for v in m.vertices:
				v = t.transformVector(v)
				fl.write('v {0} {1} {2}\n'.format(v[0], v[1], v[2]))
			for vn in m.normals:
				fl.write('vn {0} {1} {2}\n'.format(vn.x, vn.y, vn.z))
			for vt in m.texCoords:
				fl.write('vt {0} {1}\n'.format(vt.x, vt.y))
			
			if len(m.normals) != 0: hasNormals = True
			if len(m.texCoords) != 0: hasTexCoords = True
			for f in m.faces:
				l = ['f ' + str(f.vA), str(f.vB), str(f.vC)]
				# f v/vt
				if hasTexCoords:
					l[0] += '/' + str(f.vtA)
					l[1] += '/' + str(f.vtB)
					l[2] += '/' + str(f.vtC)
					# f v/vt/vn
					if hasNormals:
						l[0] += '/' + str(f.vnA)
						l[1] += '/' + str(f.vnB)
						l[2] += '/' + str(f.vnC)
				# f v//vn
				elif hasNormals:
					l[0] += '//' + str(f.vnA)
					l[1] += '//' + str(f.vnB)
					l[2] += '//' + str(f.vnC)
				fl.write(' '.join(l) + '\n')

