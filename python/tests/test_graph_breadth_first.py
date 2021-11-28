from python.code_challenges.graph_breadth_first.graph_breadth_first import Graph

from code_challenges.graph_breadth_first.graph_breadth_first import *

def test_BFS():

  obj = Graph()

  g1 = obj.add_node(1)

  g2 = obj.add_node(2)

  g3 = obj.add_node(3)

  g4 = obj.add_node(4)

  g5 = obj.add_node(5)

  obj.add_edge(g1,g2,1)


  obj.add_edge(g1,g3,2)

  obj.add_edge(g2,g4,4)

  obj.add_edge(g3,g4,8)

  obj.add_edge(g3,g5,3)

  obj.add_edge(g4,g5,5)

  obj.add_edge(g5,g1,10)

  assert obj.test_BFS(g1) == [1, 2, 3, 4, 5]

  assert obj.test_BFS(g2) == [2, 4, 1, 5, 3]

  assert obj.test_BFS(g3) == [3, 4, 5, 1, 2]

  assert obj.test_BFS(g4) == [4, 5, 3, 1, 2]

  assert obj.test_BFS(g5) == [5, 3, 4, 1, 2]
