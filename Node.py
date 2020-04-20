"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    Node.py       Authors: Eduardo Nodarse, [Add ya'lls names]
    Created: 3/22/2020
------------------------------------------------------------------------------
    Class that creates a node for a doubly-linked list as a representation
    for a polygon
------------------------------------------------------------------------------
    Edited:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
import Vertex

class Node:
    """
        Node contains 3 class attributes, a vertex, a reference to the next
        node, and a reference to the previous node that all start out as null
    """
    vertex = None
    next_node = None
    prev_node = None
    weight = 0

    def __init__(self, v):
        """Constructor that takes a vertex as a parameter and sets it to this
           node's vertex. The next and previous nodes are still null"""
        self.vertex = v

    def Add_Node(self, n):
        """Links the new node to this node"""
        #print("Adding node: {}".format(n.vertex.Display()))
        self.next_node = n
        self.next_node.prev_node = self

