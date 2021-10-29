# Stacks and Queues
<!-- Short summary or background information -->
- [x] Node : Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.
- [x] Create a Stack class that has a top property. It creates an empty Stack when instantiated. This object should be aware of a default empty value assigned to top when the stack is created.
- [x] push that take Arguments: value and adds a new node with that value to the top of the stack with an O(1) Time performance.
- [x] pop that take Arguments: none and Returns: the value from node from the top of the stack , Removes the node from the top of
the stack and Should raise exception when called on empty stack.
- [x] peek take Arguments: none , Returns: Value of the node located at the top of the stack , Should raise exception when called on empty stack.
- [x] Create a Queue class that has a front property. It creates an empty Queue when instantiated.
- [x] create  is empty  function that take Arguments: none and Returns: Boolean indicating whether or not the queue is empty
- [x]  enqueue that take Arguments: value and adds a new node with that value to the back of the queue with an O(1) Time performance.
- [x] method dequeue Arguments: none and Returns: the value from node from the front of the queue , Removes the node from the front of the queue , Should raise exception when called on empty queue.
- [x] peek , Arguments: none and Returns: Value of the node located at the front of the queue , Should raise exception when called on empty stack.


## Approach & Efficiency
### Stack
push big O(1) for space
bigO(1) for time

pop bigO(1) for space
 bigO(1) for time

peek bigO(1) for space
bigO(1) for time

is empty bigO(1) for space
 bigO(1) for time



### Queue

enqueue bigO(1) for space
bigO(1) for time

dequeue bigO(1) for space
bigO(1) for time

peek bigO(1) for space
 bigO(1) for time

is empty bigO(1) for
space bigO(1) for time



## API
<!-- Description of each method publicly available to your Stack and Queue-->

### Stack

1. push

adds a new node with that value to the top of the stack with an O(1) Time performance.
2. pop

Removes the node from the top of the stack
Should raise exception when called on empty stack
3. peek

Returns: Value of the node located at the top of the stack
Should raise exception when called on empty stack
4. is empty
Arguments: none
Returns: Boolean indicating whether or not the stack is empty.
### Queue

1. enqueue

adds a new node with that value to the back of the queue with an O(1) Time performance.
2. dequeue


Removes the node from the front of the queue
Should raise exception when called on empty queue
3. peek

Returns: Value of the node located at the front of the queue
Should raise exception when called on empty stack
4. is empty

Returns: Boolean indicating whether or not the queue is empty

