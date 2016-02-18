import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import ctypes
import math

vertexBuffer = None
indexBuffer = None
# vertices = None
# indices = None
gWorld = None
scale = 0.3
vertex_shader = """
#version 330

layout (location = 0) in vec4 pos;

uniform mat4 gWorld;

out vec4 Color;

void main()
{
    gl_Position = gWorld * vec4(pos);
    Color = vec4(clamp(vec3(pos.x, pos.y, pos.z), 0.0, 1.0), 1.0);
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
	scale += 0.001

	# mat = np.array([math.cos(scale), 0.0, 0.0, 0.0,
	# 				0.0, math.sin(scale), 0.0, 0.0,
	# 				math.cos, 0.0, math.sin(scale), 0.0,
	# 				0.0, 0.0, 0.0, 1.0], dtype=np.float32)

	mat = np.identity(4, dtype=np.float32)
	mat[0][0] = math.cos(scale)
	mat[0][2] = -math.sin(scale)
	mat[2][0] = math.sin(scale)
	mat[2][2] = math.cos(scale)

	glUniformMatrix4fv(gWorld, 1, GL_TRUE, mat)


	glEnableVertexAttribArray(0)
	glBindBuffer(GL_ARRAY_BUFFER, vertexBuffer)
	# stride is 0, offset is ctype?
	glVertexAttribPointer(0, 4, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
	glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, indexBuffer)

	# glDrawArrays(GL_TRIANGLES, 0, 3);
	glDrawElements(GL_TRIANGLES, 12, GL_UNSIGNED_INT, ctypes.c_void_p(0))

	glDisableVertexAttribArray(0);

	glutSwapBuffers()

def createVBO():
	global vertexBuffer
	# vertices = np.array([-1.0,  -1.0, 0.0, 1.0,
	# 					 1.0,  -1.0, 0.0, 1.0,
	# 					 0.0,  1.0, 0.0, 1.0], dtype=np.float32)
	vertices = np.array([-1.0,  -1.0, 0.0, 1.0,
						 0.0,  -1.0, 1.0, 1.0,
						 1.0,  -1.0, 0.0, 1.0,
						 0.0, 1.0, 0.0, 1.0], dtype=np.float32)
	vertexBuffer = glGenBuffers(1)
	glBindBuffer(GL_ARRAY_BUFFER, vertexBuffer)
	glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

def createIBO():
	global indexBuffer
	indices = np.array([0, 3, 1,
						1, 3, 2,
						2, 3, 0,
						0, 1, 2], dtype=np.uint32)

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


glClearColor(0.0, 0.0, 0.0, 0.0)

createVBO()
createIBO()

compileShaders()

initGlutCallbacks()

glutMainLoop()