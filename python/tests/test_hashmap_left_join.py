from   code_challenges.hashmap_left_join.hashmap_left_join import  HashTable , hash_left_join


def test_hash_left_join():

  obj_hashtable1 = HashTable()

  obj_hashtable1.add("fond", "enamored")

  obj_hashtable1.add("wrath", "anger")

  obj_hashtable1.add("diligent", "employed")

  obj_hashtable2 = HashTable()

  obj_hashtable2.add("fond", "averse")

  obj_hashtable2.add("wrath", "delight")

  obj_hashtable2.add("diligent", "idle")

  assert (hash_left_join(obj_hashtable1,obj_hashtable2)) == [['fond', 'enamored', 'averse'], ['wrath', 'anger', 'delight'],
['diligent', 'employed', 'idle']]
