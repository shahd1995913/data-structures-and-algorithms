from code_challenges.linked_list.linked_list import (Node,LinkedList)

# import pytest


def test_import():
    assert LinkedList



def test_node_has_int_data():
    # Arrange any data that you need to run your test
    expected = 1

    # Act on the subject of the test to produce some actual output
    node = Node(1)
    actual = node.data

    # Assert
    assert actual == expected


def test_node_has_str_data():
    # Arrange any data that you need to run your test
    expected = "a"

    # Act on the subject of the test to produce some actual output
    node = Node("a")
    actual = node.data

    # Assert
    assert actual == expected


def test_node_is_a_Node():
    # Arrange any data that you need to run your test
    expected = "Node"

    # Act on the subject of the test to produce some actual output
    node = Node(1)
    actual = type(node).__name__

    # Assert
    assert actual == expected

# def test_node_without_value():
#   with pytest.raises(TypeError):
#     node = Node()


def test_new_linked_list_is_empty():
  expected = None

  ll = LinkedList()
  actual = ll.head

  assert actual == expected



def test_linked_list_insert():
  # Arrange
  expected = 1
  ll = LinkedList()
  # Act
  actual = ll.insert(1)



def test_linked_list_insert_twice():
  # Arrange
  expected = 0
  ll = LinkedList()

  # Act
  ll.insert(1)
  ll.insert(0)
  node = ll.head
  actual = node.data

  # Assert
  assert actual == expected
  assert ll.head.next.data == 1

# test for Include Function



def test_includes():

    ll=LinkedList()
    ll.insert(1)
    ll.insert(0)

    ##
    expected=True
    actuall=ll.includes(1)
    assert actuall==expected


def test_toString():
    ll=LinkedList()
    ll.insert(1)
    ll.insert(0)

     #output
    expected= "{ 0 } -> { 1 } -> NULL"
    actul= ll.to_string()

    assert expected==actul


def test_kth1():
  linked_obj=LinkedList()
  linked_obj.insert(10)
  linked_obj.insert(20)
  linked_obj.insert(30)
  linked_obj.insert(40)
  expected=20
  actual=linked_obj.kth(1)
  assert expected==actual

def test_kth2():

  linked_obj=LinkedList()
  linked_obj.insert(10)
  linked_obj.insert(20)
  linked_obj.insert(30)
  linked_obj.insert(40)
  expected="Exception"
  actual=linked_obj.kth(-1)
  assert expected==actual



def test_kth3():
  linked_obj=LinkedList()
  linked_obj.insert(10)
  linked_obj.insert(20)
  linked_obj.insert(30)
  linked_obj.insert(40)
  expected="Exception"
  actual=linked_obj.kth(6)
  assert expected==actual


def test_kth4():

  linked_obj=LinkedList()
  linked_obj.insert(10)
  linked_obj.insert(20)
  linked_obj.insert(30)
  linked_obj.insert(40)

  expected=40
  actual=linked_obj.kth(3)
  assert expected==actual

def test_kth4():

  LinkedList_obj=LinkedList()
  LinkedList_obj.insert(1)
  expected=1
  actual=LinkedList_obj.kth(0)
  assert expected==actual



