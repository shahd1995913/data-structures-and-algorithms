class Node:

    def __init__(self,item,next=None) :

         self.next=next

         self.item=item

class Stack:


    def __init__(self):

        self.top=None


    def check_stackempty(self):

        if self.top != None:

            return False

        else:

            return True


    def push(self,value):

        contain_node=Node(value)

        if self.top:

           contain_node.next=self.top

        self.top=contain_node


