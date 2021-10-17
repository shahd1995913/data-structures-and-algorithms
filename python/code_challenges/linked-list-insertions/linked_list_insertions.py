
"""
linked-list-insertions that have 3 function :
1. append
2.  insert before
3.  insert after

"""

class Node :

    def __init__(self, info) :

         self.data = info

         self.next = None

class  linked:



    def __init__(self) :

         self.head = None

    def sortedInsert(self, new) :

        if self.head is None :

             new.next = self.head

