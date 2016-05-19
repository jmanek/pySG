import collada
import random, string
import numpy as np
from ...Math import *
def export(node, fp, options):
	debug = open(fp.replace('.dae', '_DEBUG.txt'), 'w+')
		
	def buildNode(n):

		if n.name is None: n.name = ''.join(random.choice(string.lowercase) for i in range(5))

		cNode = collada.scene.Node(n.name)
		#Create transforms
		# n.transform.updateMatrix()
		# trans = collada.scene.TranslateTransform(n.position.x, n.position.y, n.position.z)
		# print 'Euler '
		# print n.rotation.getEuler()
		# axisAngle = n.rotation.getAxisAngle()
		# print 'AA ' 
		# print axisAngle
		# print 'AA->Quat ' 
		# print Quaternion().setAxisAngle(axisAngle[0], axisAngle[1])
		# print 'AA->Quat ' 
		# print Quaternion().setAxisAngle(axisAngle[0], axisAngle[1]).getEuler()
		# rot = collada.scene.RotateTransform(axisAngle[0].x, axisAngle[0].y, axisAngle[0].z, axisAngle[1])
		# scale = collada.scene.ScaleTransform(n.scale.x, n.scale.y, n.scale.z)
		# print trans.matrix
		# print rot.matrix
		# print scale.matrix
		# n.transform.transMat * n.transform.rotMat * n.transform.sclMat
		# debug.write('\n'+n.name+'\n')
		# debug.write(str(n.rotation.getEuler())+'\n')
		# debug.write(str(n.position)+'\n')
		# print np.dot(n.transform.transMat, np.dot(n.transform.rotMat, n.transform.sclMat))
		# print len(np.dot(n.transform.transMat, np.dot(n.transform.rotMat, n.transform.sclMat)))
		# matrix = collada.scene.MatrixTransform(np.dot(n.transform.transMat, np.dot(n.transform.rotMat, n.transform.sclMat)).flatten())
		matrix = collada.scene.MatrixTransform(n.transform.matrix.flatten())
		cNode.transforms = [matrix]
		# cNode.transforms = [trans, rot, scale]
		# cNode.transforms = [scale, rot, trans]

		if n.mesh is not None:



			verts = []
			faces = []
			for v in n.mesh.vertices:
				verts.append(v.x)
				verts.append(v.y)
				verts.append(v.z)
			for f in n.mesh.faces:
				faces.append(f.vA)
				faces.append(f.vB)
				faces.append(f.vC)
			vert_src = collada.source.FloatSource(n.name+'_verts', np.array(verts), ('X', 'Y', 'Z'))
			geom = collada.geometry.Geometry(colladaDoc, n.name+'_geo'+randomString(3), n.name, [vert_src])

			input_list = collada.source.InputList()
			input_list.addInput(0, 'VERTEX', '#'+n.name+'_verts')
			tris = geom.createTriangleSet(np.array(faces), input_list, '')
			geom.primitives.append(tris)
			colladaDoc.geometries.append(geom)

			cGeomNode = collada.scene.GeometryNode(geom)
			cNode.children.append(cGeomNode)

		if n.children is not None:
			for child in n.children:
				cNode.children.append(buildNode(child))
		cNode.save()
		return cNode

	colladaDoc = collada.Collada()

	effect = collada.material.Effect("effect0", [], "phong", diffuse=(1,0,0), specular=(0,1,0))
	mat = collada.material.Material("material0", "mymaterial", effect)
	colladaDoc.effects.append(effect)
	colladaDoc.materials.append(mat)

	cNode = buildNode(node)
	scene = collada.scene.Scene('root', [cNode])
	colladaDoc.scenes.append(scene)
	colladaDoc.scene = scene
	# colladaDoc.assetInfo.upaxis = collada.asset.UP_AXIS.Z_UP
	colladaDoc.write(fp)
	debug.close()



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


def randomString(len):
	return ''.join(random.choice(string.lowercase) for i in range(len))