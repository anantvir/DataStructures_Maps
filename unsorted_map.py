"""Author - Anantvir Singh, concept and code reference:= Data Structures and Algorithms by Miachel T. Goodrich et al"""

from collections import MutableMapping
class MapBase(MutableMapping):

    class _Item:

        def __init__(self,k,v):
            self._key = k
            self._value = v

        def __eq__(self,other):
            return self._key == other._key              # compare two items based on their keys

        def __ne__(self,other):
            return not (self == other)

class UnsortedTableMap(MapBase):        # Map using unsorted list without any hashing technique
    def __init__(self):
        # create an empty map
        self._table = []
    
    def __getitem__(self,k):

        for item in self._table:
            if item._key == k:
                return item._value
    
    def __setitem__(self,k,v):
        for item in self._table:
            if item._key == k:
                item._value = v
                return      
        self._table.append(self._Item(k,v))     # Will execute this only if item is not found in the for loop above
    
    def __delitem__(self,k):
        for item in self._table:
            if item._key == k:
                ind = self._table.index(item)
                self._table.pop(ind)
                return
        raise KeyError('Key not found !')
    
    def __len__(self):
        return len(self._table)
    
    def __iter__(self):
        for item in self._table:
            yield item._key
        

m = UnsortedTableMap()
m.__setitem__(1,4)
m.__setitem__(2,8)
m.__setitem__(3,12)
m.__setitem__(4,10)
m.__setitem__(5,89)
m.__setitem__(6,1)

m.__getitem__(3)

