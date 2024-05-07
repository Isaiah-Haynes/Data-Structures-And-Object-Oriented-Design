class CustomSet:

    def __init__(self):
        self.n_buckets = 100000
        self._set = [[]for i in range(self.n_buckets)]
        self._len = 0

    def hash1(self, key):
        return hash(key) % self.n_buckets

    def add(self, key):
        bucket = self.hash1(key)       
        for item in self._set[bucket]:
            if key == item:
                return
        self._set[bucket].append(key)
        self._len += 1
    def remove(self, key):
        bucket = self.hash1(key)
        #if key in self._set[bucket]:
        try:
            #del self._set[bucket][key]
            self._set[bucket].remove(key)
        except:
            raise ValueError
        else:
            self._len -= 1
            
    def __len__(self):
        return (self._len)

    def __contains__(self, key):
        bucket = self.hash1(key)
        for item in self._set[bucket]:
            if item  == key: return True
        return False
