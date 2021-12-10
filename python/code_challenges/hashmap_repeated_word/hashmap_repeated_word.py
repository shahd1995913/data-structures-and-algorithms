"""
Write a function called repeated word that finds the first word to occur more than once in a string
Arguments: string
Return: string

"""

"""
The implementation of Node class, Linked list class, and Hashmap class.
"""

import re

class Node:
    def __init__(self, value=None, next_=None):
        """
      Initalization the Node
      """
        self.value = value
        self.next = next_




class LinkedList:
    def __init__(self):
        """
        The constructor method for the linked list. Initializes the head of a linked list to None.
        """
        self.head = None

    def insert(self, value):
        """
        Take a value and store it in a Node, then insert it to the beginning of the linked list.
        """
        self.head = Node(value, self.head)





class HashTable:
    def __init__(self, size=1024):
        """
        Initalization of Hash table
        """
        self.__size = size
        self.__buckets = [None] * size




    def __hash(self, key):
        """
        Takes a key which is a string and returns an integer which is the index that will be used to store the key/value pari in a Node at that index.
        """
        return sum([ord(char) for char in key]) * 7 % self.__size




    def add(self, key, value):
        """
        A method for adding a new value to the map
        This method should hash the key, and add the key and value pair to the table.
        Arg: Takes the key and value
        Return : No return value
        """

        index = self.__hash(key)

        if not self.__buckets[index]:
          self.__buckets[index] = LinkedList()
        my_value = [key,value]
        self.__buckets[index].insert(my_value)

    def get(self, key):
      """
      Retrieve the most recent value of in oour hasmap for the given key
      :param key str
      :rvalue any
      """
      # calculate index
      index = self.__hash(key)
      # check if there is a non empty bucket at the index
      if self.__buckets[index]:
        # iterate over linked list
        linked_list = self.__buckets[index]
        current = linked_list.head
        while current:
          # check if the key in each node matches
          if current.value[0] == key:
            # return the value of the node with the mathcing key
            return current.value[1]
          current = current.next

      # return None
      return None

      """
      create a method that called contains that take key and return T or F depend on index value
      """

    def contains(self, data_key):

      idx1 = self.__hash(data_key)

      return True if self.__buckets[idx1] else False



def hashmap_repeated_word(input_string):

    """
Write a function called repeated word that finds the first word to occur more than
 once in a string

Arguments: string     and Return: string

"""
    procesed_string = re.sub(r'[^\w\s]','',input_string).lower().split(' ')
    obj_hash_table = HashTable()
    for word in procesed_string:

        if obj_hash_table.contains(word):

            return word

        else:

            obj_hash_table.add(word,1)
    return




