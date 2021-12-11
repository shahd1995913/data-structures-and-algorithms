from code_challenges.tree_intersection.tree_intersection import treeintersection , Binary_tree , Node


def test_treeintersection():

    t1=Binary_tree()

    n1 = Node('10')

    n2 = Node('20')

    n3 = Node('30')

    n4 = Node('40')

    n1.left = n2

    n1.right = n3

    n2.left = n4

    t1.root=n1

    t2=Binary_tree()

    n1 = Node('10')

    n2 = Node('30')

    n3 = Node('50')

    n4 = Node('70')

    n1.left = n2

    n1.right = n3

    n2.left = n4

    t2.root=n1

    expected = ['10', '30']

    actual = treeintersection(t1, t2)
    assert actual == expected
