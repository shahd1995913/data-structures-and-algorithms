from code_challenges.tree_intersection.tree_intersection import *


def test_treeintersection():

    first_tree = Node(150)
    first_tree.left = Node(100)
    first_tree.left.left = Node(75)
    first_tree.left.right = Node(160)
    first_tree.left.right.left = Node(125)
    first_tree.left.right.right = Node(175)
    first_tree.right = Node(250)
    first_tree.right.left = Node(200)

    A = Binarytree(first_tree)
    scound_tree = Node(42)
    scound_tree.left = Node(100)
    scound_tree.left.left = Node(15)
    scound_tree.left.right = Node(160)
    scound_tree.left.right.left = Node(125)
    scound_tree.left.right.right = Node(175)
    scound_tree.right = Node(600)
    scound_tree.right.left = Node(200)

    B = Binarytree(scound_tree)
    assert treeintersection(A,B) == [100, 160, 125, 175, 200]
