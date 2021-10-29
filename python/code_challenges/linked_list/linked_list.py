class Node:
  """
  A class representing a Node

  Attributes
  ----------


  Methods
  -------
  __init__(data, next_):
      the constructor method for the class, it takes two parameters, the data parameter is the a reference to the data the node will hold, and the next_

  """

  def __init__(self, data, next_ = None):
    self.data = data
    self.next = next_

class LinkedList:
  """
  A class for creating instances of a Linked List.

  Data and other attributes defined here:

  head: Node | None

  Methods defined here

  insert(value: any)
  contains(value: any) -> bool
  """

  def __init__(self):

    self.head = None

    """
function inside the linked list  that  called kth that take  kth value from the end of a linked list.

"""
  def kth(self,kth_value):
    """
if the kth_value less than 0 then it will give error

      """
    if kth_value<0 :

      return "Exception"

    curr=self.head

    value_count=0

    value_counter=0

    while curr:

      if curr.next == None:

        value_counter =value_count-kth_value

        if value_counter<0:

          return "Exception"

        break

      curr=curr.next

      value_count+=1

    count=0

    curr=self.head

    while curr:

      if count == value_counter:

        return curr.data

      count+=1

      curr=curr.next

























  def insert(self, value):






    """"
    Insert creates a Node with the value that was passed and adds
    it to the head of the linked list shifting all other values down

    arguments:
    value : any

    returns: None
    """
    # create new node

    if self.head :

      self.head = Node(value, self.head)

    self.head =Node(value)


  """The Includes take  a value parameters
 and return True or False in  Boolean
 Indicates whether that value exists as a
 Node’s value somewhere within the list.

"""

  def includes(self,val):


      node_vale=self.head

  # use of while loop if the value of the head not equles to none can acecss the loop

      while node_vale != None:

        if node_vale.data==val:

             return True

        else:

           node_vale=node_vale.next

      return False


  """
 create function named is  to_string

the arguments : none  and the function return a

string representing all the values in the Linked List,

 in the following formate as below  :

"{ a } -> { b } -> { c } -> NULL"


"""

  def to_string(self):


   char1 =  ""


   node_value = self.head


  # checking if the current node value not equal None the assign new value to currentvale.data

   while node_value !=  None:

       newvale  = node_value.data


       if node_value.next is None :


# The value in linked list it will be in the formate as below  : "{ a } -> { b } -> { c } -> NULL"


          char1  += "{"+f' {newvale} '+"}"  +  " -> NULL"


          break


       else:

            char1 +="{"+f' {newvale} '+"} -> "


            node_value = node_value.next


   return char1




