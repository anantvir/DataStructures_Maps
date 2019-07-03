"""Author - Anantvir Singh, concept reference:= Data Structures and Algorithms by Michael T. Goodrich et al"""

import random
from collections import MutableMapping
class SimpleMap(MutableMapping):
    class _Item:
        def __init__(self,k,v):
            self._key = k
            self._value = v
        def __eq__(self,other):
            return self._key == other._key
        def __ne__(self,other):
            return not self == other

    def __init__(self):
        self._table = []
    
    def __len__(self):
        return len(self._table)
    
    def __getitem__(self,k):
        for item in self._table:
            if item._key == k:
                return item._value
        raise KeyError('Cannot find key !')
    
    def __setitem__(self,k,v):
        for item in self._table:
            if item._key == k:
                item._value = v
                return
        self._table.append(self._Item(k,v))
    
    def __delitem__(self,k):
        for item in self._table:
            if item._key == k:
                index = self._table.index(item)
                self._table.pop(index)
        raise KeyError('Cannot find the key to delete !')

class LinearProbingHashMap(SimpleMap):

    AVAIL_FLAG = object()                   # flag to indicate a position in table array where there was an item earlier, but now has been deleted. This is done so that while inserting a new item and finding a position to insert, we do not skip that particular array index thinking that there is no item here(Its Null) and so we declare that we cannot find the given item in the table array

    def __init__(self,init_cap = 11,p = 99999999769):
        self._table = [None] * init_cap
        self._prime = p
        self._a = 1 + random.randrange(p - 1)
        self._b = random.randrange(p)
        self._size = 0
    
    """MAD Compression function"""
    def _hash_function(self,k):
        return (hash(k)*self._a + self._b) % self._prime % len(self._table)
   
    def _is_available(self,j):      # Check if given index is avalable in table ? It contais None ? or it contains Avail flag ?
        return self._table[j] is None or self._table[j] is LinearProbingHashMap.AVAIL_FLAG

    def _find_slot(self,j,k):       # Find empty slot where a new element can be inserted
        while True:
            if self._is_available(j):
                if self._table[j] is None:
                    return (False,j)        # Return False--its not available, and 1st available index is j
            elif self._table[j]._key == k:
                return (True,j)             # Return True-- that its available at index j, change it if you want to !
            j = (j+1)%len(self._table)
    
    def _get_item_from_bucket(self,k):
        j = self._hash_function(k)
        found, index = self._find_slot(j,k) 
        if not found:                       
            raise KeyError('Cannot find the key !')
        return self._table[index]           
    
    def _set_item_into_bucket(self,k,v):
        j = self._hash_function(k)
        found, index = self._find_slot(j,k)         # find the first available slot
        if found == False:
            self._table[index] = self._Item(k,v)    # If its empty then insert new Item object at that index
        elif found == True:
            self._table[index]._value = v           # If not empty then modify the _value attribute of existing _Item object

    def _delete_item_from_bucket(self,k):
        j = self._hash_function(k)
        found,index = self._find_slot(j,k)
        if found == True:
            self._table[index] = LinearProbingHashMap.AVAIL_FLAG    # If item to be deleted is found, then put a AVail flag there
        else:
            raise KeyError('Cannot find the key to delete !')       # Raise key not found error otherwise
        
    