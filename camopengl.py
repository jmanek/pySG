import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import ctypes
import math
from Camera import Camera
from Transform import Transform

vertexBuffer = None
indexBuffer = None
# vertices = None
indices = None
gWorld = None

scale = 0.3
vertex_shader = """
#version 330

layout (location = 0) in vec3 pos;

uniform mat4 gWorld;

out vec4 Color;

void main()
{
    gl_Position = gWorld * vec4(pos, 1.0);
    Color = vec4(clamp(pos, 0.0, 1.0), 1.0);
}

"""
fragment_shader = """
#version 330

in vec4 Color;

out vec4 FragColor;

void main()
{
   FragColor = Color;
}
"""

	# FragColor = Color;

def display():
	glClear(GL_COLOR_BUFFER_BIT)

	global scale
	global tr
	scale += 1.0

	tr.rotation.setEuler(0.0, scale, 0.0)
	# tr.updateRotationMatrix()
	# c = camera.cameraTransform()
	# print 'cam rotation Mat'
	# print c[0]
	# print 'cam trans mat'
	# print c[1]
	# print 'per'
	# print camera.perspectiveTransform()
	# print 'matr'
	# print tr.matrix
	# m = camera.perspectiveTransform()*tr.transMat*tr.rotMat
	# print 'no cam'
	# print m
	m = camera.perspectiveTransform()*camera.cameraTransform()*tr.matrix
	m = m.A
	# m[3][0] = 0.0
	# m[2][3] = 2.0
	# m[3][3] = 4.0
	# m[3][3] = 1.0
	# mat = np.array([math.cos(scale), 0.0, 0.0, 0.0,
	# 				0.0, math.sin(scale), 0.0, 0.0,
	# 				math.cos, 0.0, math.sin(scale), 0.0,
	# 				0.0, 0.0, 0.0, 1.0], dtype=np.float32)

	# mat = np.identity(4, dtype=np.float32)
	# mat[0][0] = 0.5
	# mat[1][1] = 0.5

	# mat = mat*camera.perspectiveTransform() * camera.cameraTransform()
	# print mat
	glUniformMatrix4fv(gWorld, 1, GL_TRUE, m)


	glEnableVertexAttribArray(0)
	glBindBuffer(GL_ARRAY_BUFFER, vertexBuffer)
	# stride is 0, offset is ctype?
	glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
	glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, indexBuffer)

	# glDrawArrays(GL_TRIANGLES, 0, 3);
	glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, ctypes.c_void_p(0))

	glDisableVertexAttribArray(0);

	glutSwapBuffers()

def createVBO():
	global vertexBuffer
	# vertices = np.array([-1.0,  -1.0, 0.0, 1.0,
	# 					 1.0,  -1.0, 0.0, 1.0,
	# 					 0.0,  1.0, 0.0, 1.0], dtype=np.float32)
	# vertices = np.array([-1.0, -1.0,  0.5773,
	# 					 0.0,  -1.0, -1.15475,
	# 					 1.0,  -1.0,  0.5773,
	# 					 0.0,   1.0,  0.0], dtype=np.float32)
	vertices = np.array([1.0,  1.0, 1.0,
						 -1.0,  1.0, 1.0,
						 -1.0,  -1.0, 1.0,
						 1.0,  -1.0, 1.0,
						 1.0,  -1.0, -1.0,
						 1.0,  1.0, -1.0,
						 -1.0,  1.0, -1.0,
						 -1.0,  -1.0, -1.0], dtype=np.float32)
	vertexBuffer = glGenBuffers(1)
	glBindBuffer(GL_ARRAY_BUFFER, vertexBuffer)
	glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

def createIBO():
	global indexBuffer
	global indices
	# indices = np.array([0, 3, 1,
	# 					1, 3, 2,
	# 					2, 3, 0,
	# 					0, 1, 2], dtype=np.uint32)
	indices = np.array([0, 1, 2,
						0, 2, 3,
						0, 3, 4,
						0, 4, 5,
						0, 5, 6,
						0, 6, 1,
						1, 6, 7,
						1, 7, 2,
						7, 4, 3,
						7, 3, 2,
						4, 7, 6,
						4, 6, 5], dtype=np.uint32)

	indexBuffer = glGenBuffers(1)
	glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, indexBuffer)
	glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)	

def compileShaders():
	global gScale
	global gWorld
	program = glCreateProgram()
	
	vertex = glCreateShader(GL_VERTEX_SHADER)
	fragment = glCreateShader(GL_FRAGMENT_SHADER)

	glShaderSource(vertex, vertex_shader)
	glCompileShader(vertex)
	glAttachShader(program, vertex)

	glShaderSource(fragment, fragment_shader)
	glCompileShader(fragment)
	glAttachShader(program, fragment)

	glLinkProgram(program)
	glValidateProgram(program)
	glUseProgram(program)

	gWorld = glGetUniformLocation(program, 'gWorld')

def keyboard( key, x, y ):
    if key == '\033':
        sys.exit( )

def initGlutCallbacks():
	glutDisplayFunc(display)
	glutIdleFunc(display)
	glutKeyboardFunc(keyboard)
	

glutInit(sys.argv)


glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(1024, 768); 
glutInitWindowPosition(100, 100); 
glutCreateWindow('interactive')
initGlutCallbacks()

glClearColor(0.0, 0.0, 0.0, 0.0)

createVBO()
createIBO()

compileShaders()

camera = Camera()
camera.verticalFOV =90.0
camera.height = 768
camera.width = 1024
camera.near = 1.0
camera.far = 100.0
camera.position.z = -3.0
camera.target.z = 2.0

tr = Transform()
tr.position.set(0.0, 0.0, 4.0)

glutMainLoop()
# camera.target.z = 2.0
# camera.position.z = 10.0

# vpMat = camera.viewportTransform()
# perMat = camera.perspectiveTransform()
# # camMat = camera.cameraTransform()

# # print 'vp'
# # print vpMat
# print 'per'
# print perMat
# # print 'cam'
# print camMat
# m = np.identity(4)
# m[0][0] = 0.5
# m[1][1] = 0.5
# print 'identity'
# print m
# # m = perMat*m
# # m = perMat*camMat*m
# # m[2][2] = -m[2][2]
# print m