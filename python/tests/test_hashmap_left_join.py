from   code_challenges.hashmap_left_join.hashmap_left_join import *

from   code_challenges.hashmap_left_join.hashmap_left_join import HashTable , hash_left_join


def test_hash_left_join():

  first_hash = HashTable()

  first_hash.add("fond", "enamored")

  first_hash.add("wrath", "anger")

  first_hash.add("guide", "usher")

  scound_hash = HashTable()

  scound_hash.add("fond", "averse")

  scound_hash.add("wrath", "delight")

  scound_hash.add("guide", "follow")


  scound_hash.add("flow", "jam")

  assert (hash_left_join(first_hash,scound_hash)) == [['fond', 'enamored', 'averse'], ['guide', 'usher', 'follow'], ['wrath', 'anger', 'delight']]

