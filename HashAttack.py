class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Mapping:
    def __init__(self):
        self.n_buckets = 100
        self._L = [[] for i in range(self.n_buckets)]
        self._len = 0
        self._max_buckets = 1600

    def __setitem__(self, key, value):
        bucket = self.hash(key)

        # Case 1: item in mapping
        for entry in self._L[bucket]:
            if entry.key == key:
                entry.value = value
                return

        # Case 2: item not in mapping
        self._L[bucket].append(Entry(key, value))
        self._len += 1

        if (self.n_buckets < self._max_buckets and len(self) > self.n_buckets):
            self.rehash()


    def hash(self, key):
        return key % self.n_buckets

    def prime_hash(self, key, a_prime_number=1601):
        # 1) Throw a ValueError exception when the prime_number is < than the number of buckets
        # (no need to check whether the a_prime_number is actually prime)
        if a_prime_number < self.n_buckets:
            raise ValueError
        # 2) return the hash value that is equal to
        # (key mod prime_number ) mod (number of buckets)
        return ((key % a_prime_number) % self.n_buckets)

        pass
      

    def __getitem__(self, key):
        bucket = self.hash(key)
        for entry in self._L[bucket]:
            if entry.key == key: return entry.value
        raise KeyError("key {} not in Mapping".format(key))


    # Increase the number of buckets only when the
    # increase_size argument is true
    def rehash(self, increase_size = True):

        if (increase_size):
            self.n_buckets *= 2

        new_L = [[] for i in range(self.n_buckets)]

        # move all items to new list
        for bucket in self._L:
            for entry in bucket:
                new_bucket = self.hash(entry.key)
                new_L[new_bucket].append(entry)

        self._L = new_L[:]
        
    def balance(self, hash_func):
        self.hash = hash_func
        self.rehash(False)
        return
        pass

    # Return the index of the bucket with the largest number of items
    # and the number of items in that bucket
    def max_load_bucket(self):
        index = 0
        num_items_bucket = 0
        for i in range(self.n_buckets):
            if len(self._L[i]) > num_items_bucket:
                num_items_bucket = len(self._L[i])
                index = i
        return index, num_items_bucket
            
        
        pass

    # Return the index of the bucket with the largest number of items
    # and the number of items in that bucket
    def min_load_bucket(self):
        index = 0
        num_items_bucket = 2000 #this number must be exceedingly large!!!
        for i in range(self.n_buckets):
            if len(self._L[i]) < num_items_bucket:
                   num_items_bucket = len(self._L[i])
                   index = i
        return index, num_items_bucket
        pass


    def __len__(self):
        return (self._len)

"""
m is a Mapping
q is the number of key-value pairs of the form (k, str(k)) where k are integers
bucket_index is the index of the bucket to receive the q pairs mentioned above

We want all the keys to hash to the same value bucket_index assuming that the original 
hash function is in place.
"""
def hash_attack( m , q, bucket_index):
    '''    for i in range(q):
        for entry in m._L[bucket_index]:
            if entry.key == i:
                entry.value = str(i)
                return'''
    for i in range(0,q-3):        
        m._L[bucket_index].append(Entry(i, str(i)))
        m._len += 1

    if (m.n_buckets < m._max_buckets and len(m) > m.n_buckets):
        m.rehash()
    pass

if __name__ == '__main__':
    m = Mapping()                                                                   
    n = 4800                                                                        
                                                                                
    # Normal operation                                                              
    for i in range(n):                                                              
        m[i] = str(i)                                                               
                                                                                
    for i in range(n):                                                              
        assert m[i] == str(i)                                                       
                                                                                
    _, max_load = m.max_load_bucket()                                               
    _, min_load = m.min_load_bucket()                                               
                                                                                
    assert max_load == 3                                                            
    assert min_load == 3                                                            
                                                                                
    # HASH ATTACK 1: a group of hackers overload a single bucket with index 7       
    hash_attack(m, 500, bucket_index = 7)                                           
                                                                                
    max_idx2, max_load2 = m.max_load_bucket()                                       
    _, min_load2 = m.min_load_bucket()                                              
                                                                                
    assert max_idx2 == 7; assert max_load2 == 500 # Lots of collisions              
    assert min_load2 == 3;                                                          
                                                                                
                                                                                
    a_prime_number = 1601 # > m.n_buckets = 1600                                    
                                                                                
    # We will use a new hash function to re-balance our Mapping                     
    prime_hash = lambda x: m.prime_hash( x, a_prime_number)                                                                                                   
                                                                                
    m.balance(prime_hash)                                                           
                                                                                
    _, max_load3 = m.max_load_bucket()                                              
    _, min_load3 = m.min_load_bucket()                                              
    print(max_load3)
    print(min_load3)
    assert max_load3 == 7                                                           
    assert min_load3 == 3                                                           

