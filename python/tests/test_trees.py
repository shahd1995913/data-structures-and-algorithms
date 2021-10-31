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

  real = tree.inorder()

  assert real == expct


def test_post(tree):

  expct = [4, 2, 3, 1]

  real = tree.postorder()

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



# def test_Add_once():

#     tree = Binary_search()

#     tree.Add('A')

#     expected = "A"

#     actual = tree.root.value

#     assert actual == expected

# def test_Add_twice():

#     tree = Binary_search()

#     tree.Add("A")
#     tree.Add("B")

#     expected = ["A","B"]

#     actual = tree.pre()

#     assert actual == expected

# def test_contains_value():

#     tree = Binary_search()

#     tree.Add("A")
#     tree.Add("B")
#     tree.Add("C")

#     expected = True

#     actual = tree.contain("B")

#     assert actual == expected

# def test_not_contains_value():

#     tree = Binary_search()

#     tree.Add("A")
#     tree.Add("B")
#     tree.Add("C")

#     expected = False

#     actual = tree.contain("E")

#     assert actual == expected
def test_max_value():
   """
    Test max value with Tree have an elements
   """
   tree = Binary_search()
   tree.Add(1)
   tree.Add(2)
   tree.Add(3)
   tree.Add(18)
   tree.Add(15)

   #output

   expected = 18
   actul=tree.retuen_max_tree()

   assert expected==actul

def test_max_value2():
   """
    Test max value with Tree is empty
   """
   tree = Binary_search()

   #output

   expected = 0
   actul=tree.retuen_max_tree()

   assert expected==actul
