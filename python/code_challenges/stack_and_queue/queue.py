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
