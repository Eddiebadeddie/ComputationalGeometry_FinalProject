import Polygon
import Node
import Vertex

p = Polygon.Polygon()

v0 = Vertex.Vertex(0, 0)
v1 = Vertex.Vertex(1, 0)
v2 = Vertex.Vertex(0, 1)

p.Add_Vertex(v0)
print()
p.Add_Vertex(v1)
print()
p.Add_Vertex(v2)
print()

p.Connect()
p.Display()
