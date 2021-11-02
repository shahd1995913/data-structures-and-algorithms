from code_challenges.tree_fizz_buzz.tree_fizz_buzz import (Binarytrees,fizz_buzz_tree,Node)

def test():

    obj_binary_tree = Binarytrees()

    obj_binary_tree.root = Node(90)

    obj_binary_tree.root.left = Node(1)

    obj_binary_tree.root.right = Node(25)

    obj_binary_tree.root.left.right = Node(30)

    obj_binary_tree.root.left.left = Node(7)

    obj_binary_tree.root.right.right=Node(3)

    obj_binary_tree.root.right.right.left=Node(15)

    obj_binary_tree.root.left.left.right=Node(10)



    expected = ['FizzBuzz', '1', '7', 'Buzz', 'FizzBuzz', 'Buzz', 'Fizz', 'FizzBuzz']

    real = fizz_buzz_tree(obj_binary_tree)

    assert expected == real
