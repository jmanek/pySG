import string
import random
import os
import obj
# import dae

# formats = {'.obj':obj.export, '.dae': dae.export}
formats = {'.obj':obj.export}



def export(node, fp):

	ext = os.path.splitext(fp)[1]

	if ext in formats:
		formats[ext](node, fp)
	else:
		print ext +  ' not supported'











# class Export(object):

# 	@staticmethod
# 	def obj(node, fp):

# 		vO = 0
# 		vnO = 0
# 		vtO = 0
# 		vs = []
# 		vns = []
# 		vts = []
# 		fs = []
# 		materials = set()
# 		with open(fp, 'w+') as fl:

# 			for n in [node] + node.getAllChildren():
# 				if n.mesh is None: continue
# 				m = n.mesh
# 				t = n.transform
# 				t.updateMatrix()
# 				# fs.append('g {0}\n'.format(''.join(random.choice(string.lowercase) for i in range(10))))
# 				hasNormals = False
# 				hasTexCoords = False
# 				currMaterial = None
# 				mat = None

# 				for v in m.vertices:
# 					v = t.transformVector(v)
# 					# fl.write('v {0} {1} {2}\n'.format(v[0], v[1], v[2]))
# 					vs.append('v {0} {1} {2}'.format(v[0], v[2], v[1]))
# 				for vn in m.normals:
# 					vns.append('vn {0} {1} {2}'.format(vn.x, vn.y, vn.z))
# 				for vt in m.texCoords:
# 					vts.append(('vt {0} {1}'.format(vt.x, vt.y)))
				
# 				if len(m.normals) != 0: hasNormals = True
# 				if len(m.texCoords) != 0: hasTexCoords = True
# 				for f in m.faces:
# 					l = ['f ' + str(f.vA+vO), str(f.vB+vO), str(f.vC+vO)]
# 					# f v/vt
# 					if hasTexCoords:
# 						l[0] += '/' + str(f.vtA+vtO)
# 						l[1] += '/' + str(f.vtB+vtO)
# 						l[2] += '/' + str(f.vtC+vtO)
# 						# f v/vt/vn
# 						if hasNormals:
# 							l[0] += '/' + str(f.vnA+vnO)
# 							l[1] += '/' + str(f.vnB+vnO)
# 							l[2] += '/' + str(f.vnC+vnO)
# 					# f v//vn
# 					elif hasNormals:
# 						l[0] += '//' + str(f.vnA+vnO)
# 						l[1] += '//' + str(f.vnB+vnO)
# 						l[2] += '//' + str(f.vnC+vnO)

# 					mat = n.getMaterial(f)
# 					if mat is not None and (currMaterial is None or currMaterial.name != mat.name):
# 						currMaterial = mat
# 						l.insert(0, 'usemtl {0}\n'.format(currMaterial.name))
# 						materials.add(currMaterial)

# 					fs.append(' '.join(l))
# 					# fl.write(' '.join(l) + '\n')
# 				vO += len(m.vertices)
# 				vnO += len(m.normals)
# 				vtO += len(m.texCoords)

# 			if len(materials) != 0: fl.write('mtllib {0}\n'.format(os.path.splitext(fp)[0]+'.mtl'))
# 			fl.write('\n'.join(vs)+'\n')
# 			fl.write('\n'.join(vns)+'\n')
# 			fl.write('\n'.join(vts)+'\n')
# 			fl.write('\n'.join(fs))

# 		# print 'Exporting materials'
# 		# print len(materials)
# 		if len(materials) != 0:
# 			# print 'Exporting materials'
# 			with open(fp.replace('.obj', '.mtl'), 'w+') as fl:
# 				for m in materials:
# 					fl.write('\nnewmtl {0}\n'.format(m.name))
# 					if m.ambient is not None: fl.write('Ka {0} {1} {2}\n'.format(m.ambient.r, m.ambient.g, m.ambient.b))
# 					if m.diffuse is not None: fl.write('Kd {0} {1} {2}\n'.format(m.diffuse.r, m.diffuse.g, m.diffuse.b))
# 					if m.ambientMap is not None: fl.write('map_Ka {0}\n'.format(m.ambientMap))
# 					if m.diffuseMap is not None: fl.write('map_Kd {0}\n'.format(m.diffuseMap))



