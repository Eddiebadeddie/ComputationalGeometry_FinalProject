"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    TestPolygon.py       Authors: Eduardo Nodarse, [Add ya'lls names]
    Created: 3/22/2020
-----------------------------------------------------------------------------
    Class that tests polygon construction
-----------------------------------------------------------------------------
    Edited:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
import Polygon
import Node
import Vertex
import re

class TestPolygon:
    debug = False
    pass_list = []
    message_list = []

    def __init__(self, debug):
        self.debug = debug

    def Test1(self):
        #Polygon Construction
        v0 = Vertex.Vertex(0, 0)
        v1 = Vertex.Vertex(1, 0)
        v2 = Vertex.Vertex(0, 1)

        p = Polygon.Polygon()

        p.Add_Vertex(v0)
        
        self.Check_Vertex_Addition(p, 1, v0)

        #print()
        p.Add_Vertex(v1)
        self.Check_Vertex_Addition(p, 2, v1)
        #print()

        p.Add_Vertex(v2)
        self.Check_Vertex_Addition(p, 3, v2)
        #print()

        p.Connect()

        
        #checks to see if it is connected
        check = p.Get_Last_Node()
        if(check is None):
            self.Update_Lists(True, "PASS::This polygon is connected")
        else:
            self.Update_Lists(False, "FAIL::This polygon is not connected")


        v3 = Vertex.Vertex(0,0)

        if(v3.Is_Equal(v0)):
            self.Update_Lists(True, "PASS::The vertices are equal")
        else:
            self.Update_Lists(False, "FAIL::The vertices are supposed to be equal")

        if(v3.Is_Equal(v1)):
            self.Update_Lists(False, "FAIL::The vertices are equal, that's bad")
        else:
            self.Update_Lists(True, "PASS::The vertices are not equal, that's good")

        if(v3.Is_Equal(v2)):
            self.Update_Lists(False, "FAIL::The vertices are equal, that's bad")
        else:
            self.Update_Lists(True, "PASS::The vertices are not equal, that's good")

        p.Add_Vertex(v3)
        if(p.count == 3):
            self.Update_Lists(True, "PASS::The new Vertex was not added, that's good")
        elif(p.count > 3):
            self.Update_Lists(False,"FAIL::The new Vertex was added, that's bad")
        else:
            self.Update_Lists(False, "FAIL::One vertex was removed, Something's really wrong")
        
        if self.debug:
            p.Display()
        
        self.TestCrossProduct(p)

        self.Test_Results()
        self.Clear_Lists()

    def Test2(self, file_path):
        p = Polygon.Polygon()
        p.ReadInFromList(file_path)
        
        file = open(file_path, "r")
        contents = file.readlines()
        file.close()
        
        if len(contents) == p.count:
            self.Update_Lists(True, "PASS::There are {} vertices on the polygon, which is right".format(p.count))
        else:
            self.Update_Lists(False, "FAIL::There are {} vertices on the polygon, which should be {}".format(p.count, len(contents)))

        self.TestCrossProduct(p)

        self.Test_Results()
        self.Clear_Lists()

    def TestCrossProduct(self, polygon):
        #This test should pass (point inside the polygon)
        v1 = polygon.first_node.vertex
        v2 = polygon.first_node.next_node.next_node.vertex

        mid_x = (v1.x + v2.x) / 2
        mid_y = (v1.y + v2.y) / 2

        midpoint = Vertex.Vertex(mid_x, mid_y)

        test = polygon.Collision(midpoint)
        
        if test:
            self.Update_Lists(True, "PASS::" + midpoint.Display() + " Collides with the polygon, that's good")
        else:
            self.Update_List(False, "FAIL::" + midpoint.Display() + " Does not collide with the polygon, that's bad")

        #This test should fail (point outside of the polygon)
        trajectory_x = -1 * (v2.x - v1.x)
        trajectory_y = -1 * (v2.y - v1.y)

        v3 = Vertex.Vertex(v1.x + trajectory_x, v1.y + trajectory_y)

        test = polygon.Collision(v3)

        if test:
            self.Update_Lists(False, "FAIL::" + v3.Display() +" Collides with the polygon, that's bad")
        else:
            self.Update_Lists(True, "PASS::" + v3.Display() + " Does not collide with the polygon, that's good")

        #This test should pass (Point on the edge of the polygon)
        v3 = polygon.first_node.vertex

        test = polygon.Collision(v3)

        if test:
            self.Update_Lists(True, "PASS::" + v3.Display() + " Collides with the polygon, that's good")
        else:
            self.Update_Lists(False, "FAIL::" + v3.Display() + " Does not collide with the polygon, that's bad")

    def Test_Results(self):
        num = 0

        for x in range(len(self.pass_list)):
            if self.pass_list[x]:
                num += 1

            if self.debug:
                print(self.message_list[x])

        print("{}%".format((num/len(self.pass_list)) * 100))    

    def Check_Vertex_Addition(self, polygon, expected_count, excpected_vertex):
        if(polygon.count == expected_count):
            quick = polygon.Get_Last_Node()
            if(quick is not None and quick.vertex.Is_Equal(excpected_vertex)):
                self.Update_Lists(True, "PASS::Vertex was added properly, and is in correct position")
            else:
                self.Update_Lists(False, "FAIL::Vertex was added properly, but it is not in the correct place")
        else:
            self.Update_Lists(False, "FAIL::Vertex was not added")

    def Update_Lists(self, bool, message):
        self.message_list.append(message)
        self.pass_list.append(bool)

    def Clear_Lists(self):
        self.message_list.clear()
        self.pass_list.clear()