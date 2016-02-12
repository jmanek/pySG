# pySG
A scene graph for python

```python
# Build a cube and export it
import pySG

box = pySG.Node()
mesh = pySG.Mesh()

# Add some points
mesh.addVertex(-0.5000, 0.0000, 0.5000)
mesh.addVertex(-0.5000, 0.0000, -0.5000)
mesh.addVertex(0.5000, 0.0000, -0.5000)
mesh.addVertex(0.5000, 0.0000, 0.5000)
mesh.addVertex(-0.5000, 1.0000, 0.5000)
mesh.addVertex(0.5000, 1.0000, 0.5000)
mesh.addVertex(0.5000, 1.0000, -0.5000)
mesh.addVertex(-0.5000, 1.0000, -0.5000)

# Indexed vertices
mesh.addFace(1, 2, 3)
mesh.addFace(3, 4, 1)
mesh.addFace(5, 6, 7)
mesh.addFace(7, 8, 5)
mesh.addFace(1, 4, 6)
mesh.addFace(6, 5, 1)
mesh.addFace(4, 3, 7)
mesh.addFace(7, 6, 4)
mesh.addFace(3, 2, 8)
mesh.addFace(8, 7, 3)
mesh.addFace(2, 1, 5)
mesh.addFace(5, 8, 2)

box.mesh = mesh
# Add it to a parent node and apply a rotation
node = pySG.Node()
node.rotation.setEuler(45, 45, 0)
node.addChild(box)

# Export
pySG.Export.obj(node, 'box.obj')