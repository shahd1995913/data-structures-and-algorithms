
class HashTable():

  def __init__(self ,size = 1024):

    """initialization hash table"""

    self.max = size

    self.arr = [[] for i in range(self.max)]

  def get_hash(self, key):

    """function to return the hash value using ASCII code"""

    h = 0

    for char in key:

        h += ord(char)

    hash_index= h % self.max

    return hash_index

  def add(self ,key ,value):

    """Function the store key value pairs in the key index of list"""

    h = self.get_hash(key)

    found = False

    for idx, element in enumerate(self.arr[h]):

      if len(element)==2 and element[0] == key:

          self.arr[h][idx] = (key,value)

          found = True
    if not found:

      self.arr[h].append((key,value))


  def get(self, key):
      
    """function that return the value stored in the key index"""

    h = self.get_hash(key)

    for element in self.arr[h]:


      if element[0] == key:

        return element[1] # return the value

  def keys(self):
    """function that return all keys in the hash table"""

    keys = []

    for element in self.arr:

        for key in element:

            keys.append(key[0])

    return keys

def hash_left_join(first_hash,socund_hash):

    """
Write a function called left join
Arguments: two hash maps
The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
Return: The returned data structure that achieves the LEFT JOIN logic.
"""

    result = []

    for i in first_hash.keys():

        if i in socund_hash.keys():

            result.append([i, first_hash.get(i), socund_hash.get(i)])

        else:

            result.append([i, first_hash.get(i), None])

    for i in socund_hash.keys():

        if i not in first_hash.keys():

            result.append([i, None, socund_hash.get(i)])

    return result
