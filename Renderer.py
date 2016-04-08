
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from Vector2 import Vector2
from Vector3 import Vector3
import numpy as np
import ctypes
import math

class Renderer(object):

	ZOOM_MOVE = 0.5
	PAN_MOVE = 0.12


	def __init__(self, camera, node):
		self.camera = camera
		self.node = node
		
		self.setupGlut()
		self.setupCallbacks()
		self.compileShaders()
		self.buildBuffers()
		self.scale = 0.0005
		self.mouse = Vector2()

		glutMainLoop()

	def setupGlut(self):
		glutInit(sys.argv)
		glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
		glutInitWindowSize(self.camera.width, self.camera.height); 
		glutInitWindowPosition(100, 100); 
		glutCreateWindow('pySG')
		glClearColor(0.0, 0.0, 0.0, 0.0)

	def setupCallbacks(self):
		glutDisplayFunc(self.display)
		glutIdleFunc(self.display)
		glutKeyboardFunc(self.keyboard)
		glutSpecialFunc(self.keyboard)
		glutMouseFunc(self.mouse)
		glutMotionFunc(self.mouseMove)
		glutMouseWheelFunc(self.mouseWheel)
	
	def keyboard(self, key, x, y ):
		if key == '\033':
			glutLeaveMainLoop()
			# glutDestroyWindow(glutGetWindow())
			# self.camera.position -= self.camera.target.normalize() * self.CAMERA_MOVE
		# elif key == GLUT_KEY_UP:
		# elif key == GLUT_KEY_DOWN:
		# 	self.camera.position -= self.camera.up.normalize() * self.CAMERA_MOVE
		# elif key == GLUT_KEY_RIGHT:
		# elif key == GLUT_KEY_LEFT:
		# 	self.camera.position -= Vector3.cross(self.camera.up.normalize(),self.camera.target.normalize()) * self.CAMERA_MOVE
	def mouse(self, button, state, x, y):
		print button
		if button == GLUT_MIDDLE_BUTTON:
			self.mouse.set(x, y)

	def mouseMove(self, x, y):
		newMouse = Vector2(x, y)
		delta = (newMouse - self.mouse).normalize()
		self.mouse = newMouse
		if delta.x > 0:
			self.camera.position -= Vector3.cross(self.camera.up.normalize(),self.camera.target.normalize()) * delta.x * self.PAN_MOVE
		else:
			self.camera.position += Vector3.cross(self.camera.up.normalize(),self.camera.target.normalize()) * abs(delta.x) * self.PAN_MOVE
		if delta.y < 0:
			self.camera.position -= self.camera.up.normalize() * abs(delta.y) * self.PAN_MOVE
		else:
			self.camera.position += self.camera.up.normalize() * delta.y *self.PAN_MOVE
				
		print delta

	def mouseWheel(self, wheel, forward, x, y):
		print forward
		if forward == 1:
			self.camera.position += self.camera.target.normalize() * self.ZOOM_MOVE
		else:
			self.camera.position -= self.camera.target.normalize() * self.ZOOM_MOVE
	
	def compileShaders(self):
		program = glCreateProgram()
		
		vertex = glCreateShader(GL_VERTEX_SHADER)
		fragment = glCreateShader(GL_FRAGMENT_SHADER)

		glShaderSource(vertex, self.vertex_shader)
		glCompileShader(vertex)
		glAttachShader(program, vertex)

		glShaderSource(fragment, self.fragment_shader)
		glCompileShader(fragment)
		glAttachShader(program, fragment)

		glLinkProgram(program)
		glValidateProgram(program)
		glUseProgram(program)

		self.gWorld = glGetUniformLocation(program, 'gWorld')

	def buildBuffers(self):
		m = self.node.mesh
		
		self.vertices = []
		for v in m.vertices:
			self.vertices += [v.x, v.y, v.z]
		self.vertices = np.array(self.vertices, dtype=np.float32)
		self.vertexBuffer = glGenBuffers(1)
		glBindBuffer(GL_ARRAY_BUFFER, self.vertexBuffer)
		glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

		self.faces = []
		for f in m.faces:
			self.faces += [f.vA-1, f.vB-1, f.vC-1]	
		self.faces = np.array(self.faces, dtype=np.uint32)
		self.faceBuffer = glGenBuffers(1)
		glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.faceBuffer)
		glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.faces.nbytes, self.faces, GL_STATIC_DRAW)	

	def display(self):
		glClear(GL_COLOR_BUFFER_BIT)
		self.scale += 0.1
		self.node.rotation.setEuler(self.scale/2, self.scale, 0)
		m = self.camera.perspectiveTransform()*self.camera.cameraTransform()*self.node.transform.matrix
		glUniformMatrix4fv(self.gWorld, 1, GL_TRUE, m.A)

		glEnableVertexAttribArray(0)
		glBindBuffer(GL_ARRAY_BUFFER, self.vertexBuffer)
		glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
		glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.faceBuffer)
		glDrawElements(GL_TRIANGLES, len(self.faces), GL_UNSIGNED_INT, ctypes.c_void_p(0))

		glDisableVertexAttribArray(0);

		glutSwapBuffers()


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
		# FragColor = vec4(1.0, 0.0, 0.0, 1.0);