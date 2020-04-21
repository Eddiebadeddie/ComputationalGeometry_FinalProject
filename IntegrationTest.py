import TestPolygon
import graph
import Polygon
import Vertex
import sys

argc = len(sys.argv)
debug = False
debug_index = 0
polygons = []

if(argc > 1):
    for x in range(len(sys.argv)):
        if sys.argv[x] == "debug":
            debug_index = x
            debug = True

test = TestPolygon.TestPolygon(debug)

test.Test1()

for i in range(1, argc):
    print()
    
    if i == debug_index:
        continue
    
    test.Test2(sys.argv[i])
    p = Polygon.Polygon()
    p.ReadInFromList(sys.argv[i])
    polygons.append(p)

TestingGraph = graph.Graph(60,60)
#TestingGraph.Display()

for i in range(len(polygons)):
    TestingGraph.addObstacle(polygons[i])

TestingGraph.Display()
print()

start = Vertex.Vertex(0,0)

TestingGraph.WavefrontExpansion(start)
TestingGraph.Display()

end = Vertex.Vertex(50, 50)
path = TestingGraph.FindPath(start, end)


for i in range(len(path)):
    print(path[i].Display())