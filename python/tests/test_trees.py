from code_challenges.trees.trees import Node , Binary_search , Binarytrees
import pytest


@pytest.fixture

def tree():

  tree = Binarytrees()

  a_node = Node('a')


  b_node = Node('b')

  c_node = Node('c')

  d_node = Node('d')

  a_node.left = b_node

  a_node.right = c_node

  b_node.left = d_node


  tree.root=a_node

  return tree


def test_pre_order(tree):

  expected = ["a", "b", "d", "c"]

  actual = tree.pre()

  assert actual == expected

  print("test_post_order_ passed")

def test_in_order(tree):

  expected = ["d", "b", "a", "c"]

  actual = tree.inorder()

  assert actual == expected

  print("test_post_order_ passed")

def test_post_order(tree):

  expected = ["d", "b", "c", "a"]

  actual = tree.post_order()

  assert actual == expected

  print("test_post_order_ passed")


@pytest.fixture

def binary_tree():

  binary_tree = Binary_search()


  a_node = Node('A')
  b_node = Node('B')
  c_node = Node('C')
  d_node = Node('D')
  a_node.left = b_node
  a_node.right = c_node
  b_node.left = d_node


  binary_tree.root=a_node
  return binary_tree


def test_bfs(binary_tree):

  expected = ["A", "B", "C", "D"]

  actual = binary_tree.bfs()

  assert actual == expected
  print("test_bfs passed")



def test_add_once():

    tree = Binary_search()

    tree.add('A')

    expected = "A"

    actual = tree.root.value

    assert actual == expected

def test_add_twice():

    tree = Binary_search()

    tree.add("A")
    tree.add("B")

    expected = ["A","B"]

    actual = tree.pre_order()

    assert actual == expected

def test_contains_value():

    tree = Binary_search()

    tree.add("A")
    tree.add("B")
    tree.add("C")

    expected = True

    actual = tree.__contains__("B")

    assert actual == expected

def test_not_contains_value():

    tree = Binary_search()

    tree.add("A")
    tree.add("B")
    tree.add("C")

    expected = False

    actual = tree.__contains__("E")

    assert actual == expected
