from code_challenges.trees.trees import Node , Binary_search , Binarytrees
import pytest

@pytest.fixture

def tree():

  tree = Binarytrees()

  node1 = Node(1)


  node2 = Node(2)

  node3 = Node(3)

  node4 = Node(4)

  node1.left = node2

  node1.right = node3

  node2.left = node4


  tree.root=node1

  return tree


def test_pre(tree):

  expct = [1, 2, 4, 3]

  real = tree.pre()

  assert real == expct

def test_in(tree):

  expct = [4, 2, 1, 3]

  real = tree.in_order()

  assert real == expct


def test_post(tree):

  expct = [4, 2, 3, 1]

  real = tree.post_order()

  assert real == expct



@pytest.fixture

def binarytree():

  binarytree = Binary_search()



  node1 = Node(1)


  node2 = Node(2)

  node3 = Node(3)

  node4 = Node(4)

  node1.left = node2

  node1.right = node3

  node2.left = node4



  binarytree.root=node1
  return binarytree



def test_add1():

    tree = Binary_search()

    tree.Add(80)

    expext = 80

    real = tree.root.value

    assert real == expext

def test_Add_tow_time_Node():

    tree = Binary_search()

    tree.Add(10)

    tree.Add(20)

    expext = [10,20]

    real = tree.pre()

    assert real == expext

def test_contain_values():

    tree = Binary_search()

    tree.Add(10)

    tree.Add(20)

    tree.Add(70)


    expext = True

    real = tree.contain(20)

    assert real == expext

def test_non_values_contain():

    tree = Binary_search()

    tree.Add(10)

    tree.Add(20)

    tree.Add(70)

    expext = False

    real = tree.contain(250)

    assert real == expext
