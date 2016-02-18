from Camera import Camera
from Renderer import Renderer
class Scene:


	def __init__(self):
		self.camera = Camera(1024, 756)
		self.node = None

	# def add(self, node):
	# 	self.nodes.add(node)

	# def remove(self, node):
	# 	self.nodes.remove(node)


	def render(self):
		self.render = Renderer(self.camera, self.node)




