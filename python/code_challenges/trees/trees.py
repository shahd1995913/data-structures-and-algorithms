
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
        """
pre order method  root -  left - right
"""
    def pre(self, root):

        output_preorder=[]

        if root:
            """ root of tree"""
            output_preorder.append(root.value)

            """left of tree"""

            output_preorder = output_preorder + self.pre_order(root.left)

            """rifht of tree"""

            output_preorder = output_preorder + self.pre_order(root.right)


        return output_preorder


        """
        In order method    left - root - right

        """

    def inorder(self, root):

        out_inorder=[]

        if root:

            """ left """
            out_inorder = self.in_order(root.left)
            """root """
            out_inorder.append(root.value)
            """ right"""
            out_inorder = out_inorder + self.in_order(root.right)

        return out_inorder

        """
        post order which returns an array of the values,
        ordered appropriately  left- right - root

        """

def post(self, root):

        out_post=[]

        if root:
            """
left- right - root
            """

            out_post = self.post_order(root.left)

            out_post = out_post + self.post_order(root.right)

            out_post.append(root.value)

        return out_post

"""
Create a Binary Search Tree class
"""
class Binary_search(Binarytrees):
    """
Add method that Arguments: value and Return: nothing
Adds a new node with that value in the correct location in the binary search tree.
    """
    def Add(self, val):

        node = Node(val)

        if self.root == None:

            self.root = node

            return

        curr_val = self.root

        while curr_val:
            if curr_val.value < val:

                if curr_val.left:

                   curr_val = curr_val.left

                else:

                    curr_val.left = node

                    return

            if curr_val.value > val:

                if curr_val.right:

                    curr_val = curr_val.right

                else:

                    curr_val.right = node

                    return



