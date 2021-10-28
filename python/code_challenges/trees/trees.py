
"""
Create a Node class that has properties for the value stored in the node,
the left child node, and the right child node.

"""
class Node():

    def __init__(self, value=None):

        self.right = None

        self.value = value

        self.left = None

"""
__str__ method in Python represents the class objects as a
string – it can be used for classes.
"""
def __str__(self):

        return str(self.value)


"""
Create a Binary Tree class
"""
class Binarytrees():

    def __init__(self):

        self.root = None
