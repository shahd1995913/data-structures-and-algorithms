"""
  create a method that called a breadth first that take a Arguments: Node
   and Return: A collection of nodes in the order they were visited .

"""

from collections import deque

class Vertex():

  """
  Class for Adding a node to the graph
  Arguments: value
  Returns: The added node
  """

  def __init__(self,value):

    """
    Initalization for a Vertex to hold a value."""


    self.value = value

  def __str__(self):

    return str(self.value)

class Queue():


  def __init__(self):

    self.dq = deque()

  def enqueue(self,value):

    self.dq.appendleft(value)

  def dequeue(self):

    return self.dq.pop()

  def __len__ (self):


    return len(self.dq)

class Stack:

    def __init__(self):
        """
		The constructor method for the stack class and it initializes the dq property to a new double ended queue instance.
		"""
        self.dq = deque()

    def push(self, value):
        """
		Store the passed value in a node and then push the node on top of the stack.
		PARAMETERS
		----------
			value: any
				The value that will get stored in a node to be pushed on top of the stack.
		"""
        self.dq.append(value)

    def pop(self):
        """
		Return the top node in a stack.
		"""
        self.dq.pop()

class Edge:

    """
    a class for Adding a new edge between two nodes in the graph
    If specified, assigning a weight to the edge
    Arguments: 2 nodes to be connected by the edge, weight (optional)
    Returns: nothing
  """
    def __init__(self, vertex, weight):

        self.vertex = vertex

        self.weight = weight


class Graph():

  def __init__(self):


    self._adjacency_list = {}

  def add_node(self,value):
    """
      Method for Adding a node to the graph
      Arguments: value
      Returns: The added node
    """

    v = Vertex(value)

    self._adjacency_list[v] = []

    return v

  def add_edge(self,start_vertex,end_vertex,weight =0):

    """Adds an edge to the graph"""

    if start_vertex not in self._adjacency_list:

      raise KeyError('Start vertex not found in the graph')

    if end_vertex not in self._adjacency_list:

      raise KeyError('end vertex  not found in the graph')

    self._adjacency_list[start_vertex].append((str(end_vertex),weight))

  def get_nodes(self):

    """
    Method to get all nodes in Graph
    Arguments: None
    return: All nodes
    """
    return self._adjacency_list.keys()

  def neighbors(self,vertex):

    return self._adjacency_list[vertex]

  def size(self):

          return len(self._adjacency_list)

  def breadth_first_search(self, start_vertex, action=(lambda vertex: None)):

        queue = Queue()

        visited = set()

        queue.enqueue(start_vertex)

        visited.add(start_vertex)

        while len(queue):

            current_vertex = queue.dequeue()

            action(current_vertex)

            neighbors = self.get_neigbors(current_vertex)

            for edge in neighbors:

               neighbor = edge.vertex

               if neighbors not in visited:

                    visited.add(neighbor)

                    queue.enqueue(neighbors)

                    """
  create a method that called a BFS that take a Arguments: Node
   and Return: A collection of nodes in the order they were visited .

"""
#------------------- Code Challenge: Class 36------------------------------

  def BFS(self,start_node):

        result=[]

        obj_queue = Queue()

        visit_node = set()

        obj_queue.enqueue(start_node)

        visit_node.add(start_node)

        lengh =len(obj_queue)

        while lengh:

            graph_code = obj_queue.dequeue()

            result.append(graph_code)

            for g in self._adjacency_list[graph_code]:

                if g[0] not in visit_node:

                    g=g[0]

                    visit_node.add(g)

                    obj_queue.enqueue(g)

        return result
