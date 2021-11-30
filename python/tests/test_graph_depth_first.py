from code_challenges.graph_depth_first.graph_depth_first import Graph

import pytest

def test_DFS():

  obj_graph = Graph()

  num1 = obj_graph.add_node(1)

  num2 = obj_graph.add_node(2)

  num3 = obj_graph.add_node(3)

  num4 = obj_graph.add_node(4)

  num5 = obj_graph.add_node(5)


  obj_graph.add_edge(num1, num2)
## 1--->2   , 1-->4
  obj_graph.add_edge(num1, num4)
# 1-->2-->1
# 1-->2-->3
# 1 -->2-->4
# 3-->2
# 3-->5
  obj_graph.add_edge(num2,num1)

  obj_graph.add_edge(num2,num3)


  obj_graph.add_edge(num2,num4)

  obj_graph.add_edge(num3,num2)

  obj_graph.add_edge(num3,num5)

  assert obj_graph.Depth_first(num1) == [1, 2, 3, 5 , 4]
