
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
        create a function inside Binarytrees that called retuen_max_tree that return the 0

        """


    def pre(self):
        """
        print the tree in the array with use depth way as a pre order.
        """
        arr=[]
        def rec(node):
            if node:
                arr.append(node.value)
                if node.left:
                    rec(node.left)
                if node.right:
                    rec(node.right)
        rec(self.root)

        return arr


    def inorder(self):
        """
        print the tree in the array with use depth way as a In order.
        """
        arr=[]
        def rec(node):
            if node:
                if node.left:
                    rec(node.left)
                arr.append(node.value)
                if node.right:
                    rec(node.right)
        rec(self.root)

        return arr

    def post(self):
        """
        print the tree in the array with use depth way as a post order.
        """
        arr=[]
        def rec(node):
            if node:
                if node.left:
                    rec(node.left)
                if node.right:
                    rec(node.right)
                arr.append(node.value)
        rec(self.root)

        return arr


    def retuen_max_tree(self):

        if self.root == None:
          return 0
        max_val = self.root.value
        def max_fun(root):
          nonlocal max_val
          if root.value > max_val:
              max_val = root.value
          if root.left:
              max_fun(root.left)
          if root.right:
              max_fun(root.right)
          return max_val
        return max_fun(self.root)
        """
pre order method  root -  left - right
"""
#     def pre(self):

#         self.output_preorder=[]

#         def pre_inside(root):





#                 """ root of tree"""
#                 self.output_preorder.append(root.value)


#                 """left of tree"""
#                 if root.left ==

#                 self.output_preorder = self.output_preorder +pre_inside(root.left)

#                 """rifht of tree"""

#                 self.output_preorder = self.output_preorder +pre_inside(root.right)

#             print(self.output_preorder)
#         return self.output_preorder




#         """
#         In order method    left - root - right

#         """

#     def inorder(self, root=None):

#         out_inorder=[]

#         if root:

#             """ left """
#             out_inorder = self.in_order(root.left)
#             """root """
#             out_inorder.append(root.value)
#             """ right"""
#             out_inorder = out_inorder + self.in_order(root.right)

#         return out_inorder

#         """
#         post order which returns an array of the values,
#         ordered appropriately  left- right - root

#         """

#     def post(self, root):

#         out_post=[]

#         if root:
#             """
# left- right - root
#             """

#             out_post = self.post_order(root.left)

#             out_post = out_post + self.post_order(root.right)

#             out_post.append(root.value)

#         return out_post

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


                    """
Contains  method  that the Argument: value and Returns: boolean

indicating whether or not the value is in the tree at least once.

"""


    def contain(self, val):

        if val == self.root:

            return True

        curr_val = self.root

        while curr_val:


            if curr_val.value < val:

                if curr_val.left:

                   curr_val = curr_val.left

                else:

                    return False

            if curr_val.value > val:

                if curr_val.right:

                   curr_val = curr_val.right

                else:

                    return False



            if curr_val.value == val:

                return True

        return False


        """
================================ " Find the Maximum Value in a Binary Tree "================================================================
"""



