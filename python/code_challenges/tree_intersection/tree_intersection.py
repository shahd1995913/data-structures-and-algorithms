class Node:
    def __init__(self, data, left=None, right=None):

        self.data = data

        self.left = left

        self.right = right


class Queue:

    def __init__(self, collection=[]):

        self.data = collection


    def enqueue(self, item):

        self.data.append(item)

    def peek(self):

        if len(self.data):

            return True

        return False

    def dequeue(self):

        return self.data.pop(0)


class Binary_tree:

    def __init_(self):

        self.root = None


    def breadth_first_search(self):
        """
        A binary tree method which returns a list of items  in Breadth First Search Order
        args: None
        output: tree items

        """
        obj_queue = Queue()

        obj_queue.enqueue(self.root)

        if not self.root:
            return None

        l1 = []

        while obj_queue.peek():

            front = obj_queue.dequeue()

            l1 += [front.data]

            if front.left:

                obj_queue.enqueue(front.left)

            if front.right:

                obj_queue.enqueue(front.right)

        return l1


class HashNode:

    def __init__(self, value=None, next_=None):

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
        self.head = HashNode(value, self.head)




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
        return index




def treeintersection(t1, t2):
    """
Write a function called treeintersection that takes two binary trees as parameters.
 Using your Hashmap implementation as a part of your algorithm, return a set of values found in both trees.

    """

    obj_hashtable=HashTable()

    l1 = t1.breadth_first_search()

    l2 = t2.breadth_first_search()

    tree1_list = []

    tree2_list=[]

    for i in l1:

        tree1_list.append(obj_hashtable.add(i,i))

    for i2 in l2:

        idx=obj_hashtable.add(i2,i2)

        if idx in tree1_list:

            tree2_list.append(i2)

    return tree2_list
