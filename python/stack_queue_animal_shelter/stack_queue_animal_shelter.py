

class Node:
    """ self reference to object like this  """
    """  class contian all element  , Reference for all  data called class Node  """
    def __init__(self, value=None) :
        """ method called when an object is created from the class
        and it allow the class to initialize the attributes of a class"""
        self.value = value

        self.next = None

class Queue :

    def __init__(self):


        self.front = None

        self.rear = None

        """ represents the class objects as a string """
        """ This method is also used as a debugging tool when the members of a class need to be checked"""

    def __str__(self):

        cur_node = self.front

        l = []

        while cur_node :
            """  add something to list python """

            l.append(str(cur_node.value))

            cur_node = cur_node.next

        return " ".join(l)

        """  The join() method takes all items in an iterable and joins them into one string. """

    def enqueue(self, val):
        """Enqueue: Adds an item to the queue """
        node_enqueue = Node(val)

        if not self.front:

            self.front = node_enqueue

            self.rear = node_enqueue

        else:

            self.rear.next = node_enqueue

            self.rear = self.rear.next

    def dequeue(self):

        """  deque, has the feature of adding and removing elements from either end """

        if not self.is_empty():

            dequeue_node = self.front

            self.front = self.front.next

            dequeue_node.next = None

            return dequeue_node.value

    def is_empty(self):

        if self.front:

            return False

        return True

class AnimalShelter():

    def __init__(self):

        self.cat = Queue()

        self.dog = Queue()

    def enqueue(self, a):

        if a.typeofanamal == "cat":

          self.cat.enqueue(a.name)

        elif a.typeofanamal == "dog":

          self.dog.enqueue(a.name)

    def dequeue(self, pref):

        if pref == "cat":

          self.cat.dequeue()

        elif pref == "dog":

          self.dog.dequeue()

        else:

          return "null"

class Cat_animal():

  def __init__(self,name):

    self.name = name

    self.typeofanamal = "cat"

class Dog_animal():

  def __init__(self,name):

    self.name = name

    self.typeofanamal = "dog"
