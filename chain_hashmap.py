"""Author - Anantvir Singh, concept and code reference:= Data Structures and Algorithms by Michael T. Goodrich et al"""
import unsorted_map
import random
from collections import MutableMapping
class MapBase(MutableMapping):

    class _Item:
        def __init__(self,k,v):
            self._key = k
            self._value = v
        
        def __eq__(self,other):
            return self._key == other._key
        def __ne__(self,other):
            return not self == other  

class HashMapBase(MapBase):
    """Abstract Base class using hastable and MAD compression function which is [(a*i + b) mod p] mod N, where N= size of bucket array-- table in this case, p = prime number greater than N, a and b are integers in range [0,p-1] and a>0"""

    def __init__(self,init_cap = 11,prime_number = 10051949): # Capacity of bucket array should be a prime number for minimum collisions and optimal hashing performance
        self._table = [None] * init_cap
        self._size = 0
        self._prime = prime_number
        self._a = 1 + random.randrange(prime_number -1)         # added 1 since a > 0
        self._b = random.randrange(prime_number - 1)
    
    def _hash_function(self,k):
        return (hash(k)*self._a + self._b) % self._prime % len(self._table)
    
    def __len__(self):
        return self._size
    
    def __getitem__(self,k):
        hashed_index = self._hash_function(k)
        return self._get_item_from_bucket(hashed_index,k)
    
    def __setitem__(self,k,v):
        hashed_index = self._hash_function(k)
        self._set_item_into_bucket(hashed_index,k,v)
        if self._size > len(self._table) // 2:
            self._resize(2*len(self._table) - 1)
    
    def _resize(self,cap):
        old = list(self.items())
        self._table = [None] * cap
        self._size = 0
        for k,v in old:
            self[k] = v

class ChainHashMap(HashMapBase):
    """Hash map implemented with seperate chaining for collision minimisation"""
    def _get_item_from_bucket(self,hashed_index,k):         # We assume that each bucket has its own secondary container
        bucket = self._table[hashed_index]                  # holding values(k,v) in a list. So after we find this bucket
        if bucket is None:                                  # we can access the element by bucket[k]
            raise KeyError('Cannot find this key !')
        return bucket[k]
    
    def _set_item_into_bucket(self,j,k,v):
        if self._table[j] is None:
            self._table[j] = unsorted_map.UnsortedTableMap()
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize:
            self._size += 1
    
    def _del_from_bucket(self,j,k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Cannot find the item to delete !')
        del bucket[k]


