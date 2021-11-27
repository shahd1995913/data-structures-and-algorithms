import pytest
from code_challenges.hashtable.hashtable import (Node, LinkedList, HashTable)

@pytest.fixture
def hashtable():
	return HashTable()

def test_hash(hashtable):
	expected = 700
	actual = hashtable._HashTable__hash("d")
	assert actual == expected

def test_hash_word(hashtable):
	expected = 376
	actual =  hashtable._HashTable__hash("dd")
	assert actual == expected

"""
"a"
ord("d") = 100
100 * 7 = 700
700 % 1024 = 700

-----------------
"dd"
200
200 * 7 = 1400
1400 % 1024 = 376
"""

def test_key_value_adding():

  hash_obj = HashTable()

  hash_obj.add('shahed','26')

  assert hash_obj.get('shahed') == '26'

def test_key_value2():

  hash_obj = HashTable()

  hash_obj.add('Ali','26')

  assert hash_obj.get('Ali') == '26'

def test_key_None():

  hash_obj = HashTable()

  assert hash_obj.get('test') == None

def test_collision_key_values():

  hash_obj = HashTable()

  hash_obj.add('shahed','26')

  hash_obj.add('Waed','21')

  print(hash_obj.contains('shahed'))

  print(hash_obj.contains('Waed'))

def test_collision_HT():

  hash_obj = HashTable()

  hash_obj.add('shahed','26')

  hash_obj.add('Waed','21')

  assert hash_obj.get('shahed') == '26'

  assert hash_obj.get('Waed') == '21'
