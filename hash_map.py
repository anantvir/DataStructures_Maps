from collections import MutableMapping
import random
class SimpleMap(MutableMapping):
    class Item:
        def __init__(self,k,v = None):
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
        raise KeyError('Cannot find the given key !')
    
    def __setitem__(self,k,v):
        for item in self._table:
            if item._key == k:
                item._value = v
                return
        self._table.append(self.Item(k,v))
    
    def __delitem__(self,k):
        for item in self._table:
            if item._key == k:
                ind = self._table.index(item)
                self._table.pop(ind)
        raise KeyError('Cannot find the key !')
    
    def __iter__(self):
        pass

class HashMap(SimpleMap):
    def __init__(self,init_cap = 11,prm = 10051949):
        self._table = [None] * init_cap
        self._size = 0
        self._a = 1 + random.randrange(prm - 1)
        self._b = random.randrange(prm - 1)
        self._prime_number = prm
    
    def _hash_function(self,k):
        print(hash(k)*self._a + self._b% self._prime_number)
        return (hash(k)*self._a + self._b) % self._prime_number % len(self._table)
    
    def __len__(self):
        return self._size
    
    def _set_item_into_bucket(self,k,v):
        j = self._hash_function(k)
        if self._table[j] is None:
            self._table[j] = SimpleMap()
        self._table[j][k] = v
    
    def _get_item_from_bucket(self,k):
        j = self._hash_function(k)
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Cannot find key !')
        return bucket[k]
    
    def _delete_item_from_bucket(self,k):
        j = self._hash_function(k)
        if self._table[j] is None:
            raise KeyError('Key not found. Cannot delete this key !')
        del self._table[j][k]
    

m = HashMap()
m._set_item_into_bucket(1,'New York')
m._set_item_into_bucket(2,'Newark')
m._set_item_into_bucket(3,'Philadephia')
m._set_item_into_bucket(4,'Wilmington')
        


        