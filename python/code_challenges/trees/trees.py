from code_challenges.stack_and_queue.stack_and_queue import (Stack,Queue)
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
Create a Binarytrees class that have a 4 method  pre  and post and in order and max and Breadth_First_Search for finding the max value in tree
"""
class Binarytrees():

    def __init__(self):

        self.root = None
    """
define a function called a bfs_queue_First_Search(BFS) that take a Arguments: tree
and Return: list of all values in the tree, in the order they were encountered

    """

    def Breadth_First_Search(self,node):

            arr =[]

            bfs_queue = Queue()

            bfs_queue.enqueue(node)

            try:

                while bfs_queue.peek():

                    start = bfs_queue.dequeue()

                    arr.append(start.value)

                    if start.right:

                        bfs_queue.enqueue(start.right)

                    if start.left:

                        bfs_queue.enqueue(start.left)


            except AttributeError :

                pass

            return arr
            """
    End of function called Breadth_First_Search


            """


    def in_order(self):

        list=[]

        def inside_fun(node):

            if node:

                if node.left:

                    inside_fun(node.left)

                list.append(node.value)

                if node.right:

                    inside_fun(node.right)

        inside_fun(self.root)

        return list



    def pre(self):

        list=[]

        def inside_fun(node):

            if node:

                list.append(node.value)

                if node.left:

                    inside_fun(node.left)

                if node.right:

                    inside_fun(node.right)

        inside_fun(self.root)

        return list



    def post_order(self):

        list=[]

        def inside_fun(node):

            if node:


                if node.left:

                    inside_fun(node.left)

                if node.right:

                    inside_fun(node.right)



                list.append(node.value)

        inside_fun(self.root)

        return list






class Binary_search(Binarytrees):
      """
Adds a new node with in the binary search tree by create a Add method  that take a value and add it to binary tree
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
