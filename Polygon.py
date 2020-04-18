"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    Polygon.py      Authors: Eduardo Nodarse, [Add ya'lls names]
    Created: 3/22/2020
------------------------------------------------------------------------------
    Class that creates a representation of a polygon via a doubly linked list
    and keeps track of the number of vertices (or nodes) in the polygon
------------------------------------------------------------------------------
    Edited:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
import Node
import Vertex

class Polygon:
    """
        Polygon will keep a reference to the first node (v0) of the polygon.
        The rest of the nodes are accesible through here
    """
    first_node = None
    count = 0

    def __init__(self):
        super().__init__()

    def Add_Vertex(self, v):
        """"Adds a vertex at the end of this polygon"""
        
        #print("\n--Add_Vertex: {}".format(v.Display()))
        if self.Empty():
            self.first_node = Node.Node(v)
            #print("Assigned first Node: {}".format(self.first_node.vertex.Display()))

        else:
            cur = self.Get_Last_Node()
            
            if cur is not None:
                #print("Last Node: {}".format(cur.vertex.Display()))
                
                cur.vertex.Display()
                cur.Add_Node(Node.Node(v))
                
                #print("Added vertex: {}".format(v.Display()))
            else:
                #if there is a cycle, just return
                return
                
        self.count = self.count + 1


    def Get_Last_Node(self):
        #print("\n--Get_Last_Node:")
        if self.Empty():
            return None

        cur = self.first_node
        while cur.next_node is not None:
            #print("cur = {}".format(cur.vertex.Display()))
            if cur is self.first_node and cur.prev_node is not None:
                #print("There is no last node")
                return None
            
            cur = cur.next_node
        
        #print("returning {}\n".format(cur.vertex.Display()))
        return cur

    def Empty(self):
        if self.first_node is None:
            return True
        else:
            return False

    def Connect(self):
        last = self.Get_Last_Node()

        if last is None:
            print("Already connected")
            return

        last.next_node = self.first_node
        self.first_node.prev_node = last

    def Collision(self, point):
        #print("Polygon::Collision::")
        if self.first_node is None:
            print("This polygon is empty")
            return
        
        next_node = self.first_node.next_node
        #print("\tfirst_node = " + self.first_node.vertex.Display())
        #print("\tnext_node = " + next_node.vertex.Display())

        tempx = next_node.vertex.x - self.first_node.vertex.x
        tempy = next_node.vertex.y - self.first_node.vertex.y

        a = Vertex.Vertex(tempx, tempy)
        #print("\ta = " + a.Display())

        tempx = point.x - next_node.vertex.x
        tempy = point.y - next_node.vertex.y

        b = Vertex.Vertex(tempx, tempy)
        #print("\tb = " + b.Display())

        test = self.Cross(a,b)
        if test < 0:
            #print("\t" + point.Display() + " does not collide")
            return False
        
        cur = next_node
        while cur is not self.first_node:
            if(cur.next_node is None):
                print("Something is wrong, next node is null")
            next_node = cur.next_node

            tempx = next_node.vertex.x - cur.vertex.x
            tempy = next_node.vertex.y - cur.vertex.y

            a = Vertex.Vertex(tempx, tempy)
        
            tempx = point.x - next_node.vertex.x
            tempy = point.y - next_node.vertex.y

            b = Vertex.Vertex(tempx, tempy)
            #print("\tTesting " + a.Display() + " x " + b.Display())
            test = self.Cross(a,b)
            if test < 0:
                #print("\t" + point.Display() + " does not collide")
                return False
            cur = next_node

        return True

    def Cross(self, a, b):
        #print("Polygon::Cross")
        return (a.x * b.y) - (a.y * b.x)

    def Display(self):
        if self.Empty():
            print("Empty")
            return
        
        print(self.first_node.vertex.Display())
        cur = self.first_node.next_node
        while cur is not None and cur is not self.first_node:
            print(cur.vertex.Display())
            cur = cur.next_node

        print("Vertex Count: {}".format(self.count))