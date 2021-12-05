# Graphs
<!-- Short summary or background information -->


## Implement Graph. The graph should be represented as an adjacency list, and should include the following methods:

1. add node
Arguments: value
Returns: The added node
Add a node to the graph
2. add edge
Arguments: 2 nodes to be connected by the edge, weight (optional)
Returns: nothing
Adds a new edge between two nodes in the graph
If specified, assign a weight to the edge
Both nodes should already be in the Graph
3. get nodes
Arguments: none
Returns all of the nodes in the graph as a collection (set, list, or similar)
4. get neighbors
Arguments: node
Returns a collection of edges connected to the given node
Include the weight of the connection in the returned collection
5. size
Arguments: none
Returns the total number of nodes in the graph

## Challenge
<!-- Description of the challenge -->

- [x] Node can be successfully added to the graph
- [x] An edge can be successfully added to the graph
- [x] A collection of all nodes can be properly retrieved from the graph
- [x] All appropriate neighbors can be retrieved from the graph
- [x] Neighbors are returned with the weight between nodes included
- [x] The proper size is returned, representing the number of nodes in the graph
- [x] A graph with only one node and edge can be properly returned
An empty graph properly returns null


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

1. add node: Time:O(1) space:O(1)

2. add edge: Time:O(1) space:O(1)

3. get nodes: Time:O(1) space:O(1)

4. get neighbors: Time:O(1) space:O(1)

5. size: Time:O(1) space:O(1)

## API
<!-- Description of each method publicly available in your Graph -->
1. add node : Add a node to the graph
2. add edge : Adds a new edge between two nodes in the graph
If specified, assign a weight to the edge
Both nodes should already be in the Graph
3. get nodes : Returns all of the nodes in the graph as a collection
4. get neighbors : Returns a collection of edges connected to the given node

5. size : Returns the total number of nodes in the graph
