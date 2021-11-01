"""
Implement a Queue using two Stacks.


"""


class queue:


    def __init__(self):


        self.stack1 = []

        self.stack2 = []


    def enqueue(self, value):

        """
        transfer the data element from stack 1 to stack 2
        """


        while len(self.stack1) != 0:

            self.stack2.append(self.stack1[-1])

            self.stack1.pop()
            """
            Push  the element to stack 1
            """





        self.stack1.append(value)
        """

        Push the all data to stack 1 also
        """




        while len(self.stack2) != 0:

            self.stack1.append(self.stack2[-1])


            self.stack2.pop()

            """
            dequeue element from the queue

            """


    def dequeue(self):




        if len(self.stack1) == 0:

            print("Queue is not contain any data")


        value = self.stack1[-1]

        self.stack1.pop()

        return value


# if __name__ == '__main__':

#     queu1 = queue()

#     queu1.enqueue(20)

#     queu1.enqueue(15)

#     queu1.enqueue(20)


#     print(queu1.dequeue())

#     print(queu1.dequeue())

#     print(queu1.dequeue())

