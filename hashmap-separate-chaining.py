from random import randrange
from unsorted_map import UnsortedTableMap

class HashMapSeparateChaining:
    # Hashtable with MAD compression
    def __init__(self, capacity, p = 109345121):
        self._table = capacity * [None]
        self._n = 0
        self._prime = p
        self._scale = 1 + randrange(p-1)
        self._shift = randrange(p)
    
    def _hash_function(self, k):
        return (hash(k)*self._scale + self._shift) % self._prime % len(self._table)
    
    def __len__(self):
        return self._n
    
    # Wrapper over bucket_get_item method
    def __getitem__(self, k):
        j = self._hash_function(k)
        return self.bucket_get_item(j,k)
    
    # checks if bucket exists, if yes then returns data
    def bucket_get_item(self,j,k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key '+ k +' does not exist !')
        return bucket[k]
    
    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self.bucket_set_item(j, k, v)

    def bucket_set_item(self, j, k, v):
        bucket = self._table[j]
        if bucket is None:
            self._table[j] = UnsortedTableMap()
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize:
            self._n += 1
    
    def __delitem__(self, k):
        j = self._hash_function(k)
        self.bucket_delete_item(j, k)
        self._n -= 1

    def bucket_delete_item(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key '+ k +' does not exist !')
        del bucket[k]          


hm = HashMapSeparateChaining(10)
hm.__setitem__(24, "anantvir")
hm.__setitem__(67,"mayank")
hm.__setitem__(79,"nikita")
hm.__setitem__(15,"suraj")
hm.__setitem__(99,"gurjeet")

print(hm.__getitem__(67))

hm.__delitem__(15)

print("finished")

