class Node:

    def __init__(self, item):

        self.next = None

        self.item = item

class Queue:

    def __init__(self):

        self.front = self.rear = None

        """
       create  is empty  function that take Arguments: none and Returns: Boolean indicating whether or not the queue is empty
        """

    def is_empty(self):

        return self.front == None


    def enqueue(self, value):

        t = Node(value)

        if self.rear == None:

            self.front = self.rear = t

            return

        self.rear.next = t

        self.rear = t


    def dequeue(self):


        if self.is_empty():


          return "queue is null"


        t = self.front


        self.front = t.next


        if(self.front == None):


            self.rear = None

    def peek(self):

        if self.is_empty():

            return "queue is null"

        else:

            return self.front.item
