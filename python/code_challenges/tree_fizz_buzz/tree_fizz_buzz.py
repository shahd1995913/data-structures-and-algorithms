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
        self.result = []

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





        """

============================================tree-fizz-buzz ==lab 2021-11-2============================================
"""

"""

create a function that called a fizz_buzz that determine whether or not the value of each node is divisible by 3, 5 or both

"""
def fizz_buzz(num):

    if num.value %3 == 0:

        return'Fizz'

    elif num.value % 15 == 0:

        return'FizzBuzz'

    elif num.value % 5 == 0:

        return'Buzz'

    else:

        return str(num.value)
"""
create  a function called fizz_buzz_tree that take Arguments: k-ary tree and Return: new k-ary tree

"""
def fizz_buzz_tree(tree):

    if not tree.root:

        return []

    bt_obj = Binarytrees()

    def new_tree(node):

        bt_obj.result = bt_obj.result + [fizz_buzz(node)]

        if node.right:

            new_tree(node.right)

        if node.left:

            new_tree(node.left)


        return bt_obj.result

    return new_tree(tree.root)


