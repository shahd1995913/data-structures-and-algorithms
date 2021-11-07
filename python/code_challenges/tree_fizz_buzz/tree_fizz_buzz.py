
class Node:
    def __init__(self,value=None):
        self.value = value
        self.kth = []
class Kth_tree:
    def __init__(self):
        self.root = None
def fizz_buzz_tree(root):
        if root == None:
            return root
        value_crr = root
        arr = []
        arr.append(value_crr)
        while len(arr) != 0 :
            value_crr = arr.pop(0)
            if value_crr.value % 15==0:
                value_crr.value = 'FizzBuzz'
            elif value_crr.value % 3 == 0:
                value_crr.value = 'Fizz'
            elif value_crr.value % 5 == 0:
                value_crr.value = 'Buzz'
            else:
                value_crr.value = str(value_crr.value)
            for node in value_crr.kth:
                arr.append(node)
        return root


