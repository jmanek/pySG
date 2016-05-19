# from IO import IO
# from Scene import Scene

import pySG
n = pySG.load('box.obj')
n.position.z += 3.0
s = pySG.Scene()
s.node = n
s.camera.position.z -= 2.0

s.render()