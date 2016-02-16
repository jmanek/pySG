from Node import Node
from Mesh import Mesh
from Face import Face
from Material import Material
from Color import Color

import os

class Import(object):

	@staticmethod
	def obj(fp):
		
		node = Node()
		node.mesh = Mesh()
		with open(fp) as f:
			material = None
			for line in f:
				line = line.strip().split(' ', 1)
				if len(line) == 1: continue
				key, line = line[0], line[1].lstrip()
				if '#' in key: continue
				if 'vn' in key:
					line = line.split(' ')
					node.mesh.addNormal(line[0], line[1], line[2])
				elif 'vt' in key:
					line = line.split(' ')
					node.mesh.addTexCoord(line[0], line[1])
				elif 'usemtl' in key:
					material = None
					for mat in node.materials:
						if line == mat.name:
							material = mat
					if material is None:
						material = Material()
						material.name = line
						node.materials[material] = set()

				elif 'f' in key:
					line = line.split(' ')
					face = Face()
					if material is not None: node.materials[material].add(face)
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
						face.vA = int(line[0])
						face.vB = int(line[1])
						face.vC = int(line[2])	

					node.mesh.faces.append(face)
				elif 'v' in key:
					line = line.split(' ')
					node.mesh.addVertex(line[0], line[1], line[2])


		if os.path.isfile(fp.replace('.obj', '.mtl')):
			with open(fp.replace('.obj', '.mtl')) as f:
				material = None
				for line in f:
					line = line.strip().split(' ', 1)
					if len(line) == 1: continue
					key, line = line[0], line[1].lstrip()
					if '#' in key: continue
					if 'newmtl' in key:
						for mat in node.materials:
							if mat.name == line: material = mat
					if 'map_Kd' in key:
						material.diffuseMap = line
					elif 'map_Ka' in key:
						material.ambientMap = line
					elif 'Ka' in key:
						line = line.split(' ')
						material.ambient = Color(line[0], line[1], line[2])
					elif 'Kd' in key:
						line = line.split(' ')
						material.diffuse = Color(line[0], line[1], line[2])
		return node






