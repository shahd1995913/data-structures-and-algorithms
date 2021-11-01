class Node:

    def __init__(self, value):

        self.value = value

        self.next = None



class Stack:

    def __init__(self):

        self.top = None

    def pop(self):



        if not self.top :

            raise AttributeError ('Exception')

        else:

            t = self.top


            self.top = self.top.next

            t.next = None

            return t.value

    def push(self, data):

        node_data = Node(data)

        if self.top:

            node_data.next = self.top

        self.top = node_data






    def peek(self):

        if not self.is_empty():

            return self.top.value

        else :

            raise AttributeError ('Exception')

    def is_empty(self):

        if self.top:

            return False

        else:

            return True









class Queue:

    def __init__(self):

        self.rear = None

        self.front = None



    def dequeue(self):


        t = self.front

        if self.is_empty():

            raise AttributeError ('Exception')

        else:


            self.front = self.front.next

            t.next = None

        if self.front == None:

            self.rear = None

        return t.value



    def enqueue(self, data):

        node_data = Node(data)

        if self.rear:

            self.rear.next = node_data

            self.rear = node_data

        else:

            self.front = node_data

            self.rear = node_data

    def peek(self):

        try:

            return self.front.value

        except AttributeError:

            raise AttributeError ('Exception')

    def is_empty(self):

        if self.rear == None and self.front == None :

            return True

        else:

            return False

    def print_(self):

        t = self.front

        str = ''

        while t:

            str += f'{t.value} - > '

            t = t.next

        return str


