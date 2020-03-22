"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    Vertex.py       Authors: Eduardo Nodarse, [Add ya'lls names]
    Created: 3/22/2020
------------------------------------------------------------------------------
    Class that creates Vertices for polygons. Can also double as a cartesian
    point
------------------------------------------------------------------------------
    Edited:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
class Vertex:
    """
        Vertex has an x and a y integer value to represent coordinates
    """
    def __init__(self, x, y):
        """Constructor that takes an x and a y in and assigns it to this
           vertex's x and y points"""
        self.x = x
        self.y = y
    
    def Display(self):
        """returns a string to display the coordinates of this vertex"""
        return "({} , {})".format(self.x, self.y)

    def Is_Equal(self, v):
        if v.x is self.x:
            if v.y is self.y:
                return True
        
        return False