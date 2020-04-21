from array import *
import Polygon
import Node
import Vertex
import queue


class InputError (Exception):
    def __init__(self, message):
        self.message = message

class Graph:

    obstacles = []
    graph = []
    maxX = 0
    maxY = 0

    def __init__(self, x, y):
        super().__init__()
        if x <= 0 or y <= 0:
            raise InputError("({} , {}):: both must be positive".format(x,y))
        
        self.maxX = x
        self.maxY = y

        for i in range (self.maxX):
            tempNodes = []
            for j in range(self.maxY):
                n = Node.Node(Vertex.Vertex(i,j))
                tempNodes.append(n)   
            
            self.graph.append(tempNodes)

    def addObstacle(self, polygon):
        """
            Checking to see if the obstacle is within the bounding box
        """
        cur = polygon.first_node

        for i in range(polygon.count):
            if cur.vertex.x < 0 or cur.vertex.x >= self.maxX or cur.vertex.y < 0 or cur.vertex.y >= self.maxY:
                print("This obstacle exceeds the bounds")
                return
            cur = cur.next_node

        """
            Marks the occupied nodes as having a polygon
        """
        for y in range(self.maxY):
            for x in range(self.maxX):
                if(polygon.Collision(self.graph[y][x].vertex)):
                    self.graph[y][x].weight = -1



    #TODO: Wavefront Expansion
    def WavefrontExpansion(self, start):  
        #starting point is 1
        self.graph[start.y][start.x].weight = 1
        q = queue.Queue()
        q.put(start)
        while not q.empty():
            #while q is not empty dequeue first point
            curr = q.get()
            #double for loop to find vertices surrounding curr point
            for i in range(-1,2):
                for j in range(-1,2):
                    #if point is in bounds then this point is new curr
                    if(curr.y + i < self.maxY and curr.y + i >= 0 and curr.x + j < self.maxX  and curr.x + j >= 0):

                        print("\t\tInspecting ({},{}) = {}".format(curr.y + i, curr.x + j, self.WeightAt(curr.y + i, curr.x + j)))
                       
                        #curr = self.graph[curr.y + i][curr.x + j]
                        #if point is not colliding w obstacle and not already found then add to q and inc weight
                        if self.WeightAt(curr.y + i, curr.x + j) == 0:
                            self.graph[curr.y + i][curr.x + j].weight = self.WeightAt(curr.y, curr.x) + 1
                            q.put(self.graph[curr.y + i][curr.x + j].vertex)
                            print("Added ({}, {}) = {} to the q".format(curr.y + i,curr.x + j, self.WeightAt(curr.y + i, curr.x + j)))

            for q_item in q.queue:
                print (q_item.Display())
        
        exit()

    #"""
    #TODO: Djikstra's Algo
    def FindPath(self, start, end):
        path = [end]

        cur = end
        min_weight = self.WeightAt(end.y, end.x)
        min_x = end.x
        min_y = end.y
        
        for x in self.obstacles:
            if x.Collision(start):
                raise InputError("No path, start point in obstacle")
            if x.Collision(end):
                raise InputError("No path, end point in obstacle")

        while not cur.Is_Equal(start):
            old_min_x = min_x
            old_min_y = min_y

            for y in range(cur.y - 1, cur.y + 2):
                for x in range(cur.x - 1, cur.x + 2):
                    #If the cell in question is outside of the bounds
                    if x < 0 or x >= self.maxX or y < 0 or y >= self.maxY:
                        continue

                    #If the cell is part of an obstacle
                    if self.WeightAt(y, x) < 0:
                        continue
                    
                    if self.WeightAt(y,x) < min_weight:
                        min_weight = self.WeightAt(y, x)
                        min_x = x
                        min_y = y
            
            if old_min_x == min_x and old_min_y == min_y:
               raise InputError("Path is blocked")

            cur = self.VertexAt(min_y, min_x)
            path.append(cur)

        return path
    #"""  

    def WeightAt(self, y, x):
        return self.graph[y][x].weight

    def VertexAt(self, y, x):
        return self.graph[y][x].vertex


    def Display(self):
        for y in range(self.maxY):
            for x in range(self.maxX):
                print("{}".format(self.graph[y][x].weight), end = " ")
            print()
        