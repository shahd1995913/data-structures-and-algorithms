
class Node:
    """ self reference to object like this  """
    """  class contian all element  , Reference for all  data called class Node  """
    def __init__(self, value=None):
        """ method called when an object is created from the class
        and it allow the class to initialize the attributes of a class"""
        self.value = value

        self.next = None

class Queue:

    def __init__(self):


        self.front = None

        self.rear = None
        """ represents the class objects as a string """
        """ This method is also used as a debugging tool when the members of a class need to be checked"""
    def __str__(self):

        current = self.front

        items = []

        while current:
            """  add something to list python """


