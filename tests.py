from Import import Import
from Scene import Scene

n = Import.obj('box.obj')
n.position.z += 3.0
s = Scene()
s.node = n
s.camera.position.z -= 2.0

s.render()