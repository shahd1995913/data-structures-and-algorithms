
class Node:

    def __init__(self, data):

         self.data = data

         self.next = None




class linkedList:
    def __init__(self):

         self.head = None


def Pushing(self, data):

         node = Node(data)

         node.next = self.head

         self.head = node
