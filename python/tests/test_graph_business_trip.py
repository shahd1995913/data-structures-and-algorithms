from code_challenges.graph_business_trip.graph_business_trip import *
from code_challenges.graph_business_trip.graph_business_trip import businestrip


def test_businesstrip():

  obj_graph = Graph()


  Amman = obj_graph.add_node('Amman')

  Irbid = obj_graph.add_node('Irbid')

  Aqaba = obj_graph.add_node('Aqaba')

  Aydon = obj_graph.add_node('Aydon')


  obj_graph.add_edge(Amman,Irbid,1)

  obj_graph.add_edge(Amman,Aqaba,2)

  obj_graph.add_edge(Irbid,Aqaba,3)

  obj_graph.add_edge(Irbid,Aydon,4)

  obj_graph.add_edge(Aqaba,Aydon,5)


  data1 = [Amman,Irbid]

  assert obj_graph.business_trip(data1) == (True, '$1')
