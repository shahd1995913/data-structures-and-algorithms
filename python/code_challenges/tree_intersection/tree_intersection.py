"""

Write a function called treeintersection that
takes two binary trees as parameters.
 and  return a set of values found in both trees.

"""


class Node():


    def __init__(self, value=None):


        self.left = None

        self.value = value

        self.right = None

    def __str__(self):

        return str(self.value)

class Binarytree():

    def __init__(self, root=None):

        self.root = root

    def pre(self):

        result = []

        if self.root == None:


            return result

        def pre_order(root):

            result.append(root.value)

            if root.left:

                pre_order(root.left)

            if root.right:

                pre_order(root.right)


        pre_order(self.root)

        return result


def treeintersection(first_tree,scound_tree):

      result = []

      if first_tree.root == None or scound_tree.root == None:

        return None

      def intersection(first_root,scound_root) :

        if first_root.value == scound_root.value:

          result.append(first_root.value)

        if first_root.left and scound_root.left:

          intersection(first_root.left ,scound_root.left)

        if first_root.right and scound_root.right :

          intersection(first_root.right ,scound_root.right)

      intersection(first_tree.root,scound_tree.root)


      return result
