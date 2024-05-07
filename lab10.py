class Entry:
    def __init__(self, item, priority):
        self.priority = priority
        self.item = item

    def __lt__(self, other):
        return self.priority < other.priority

    def __eq__(self, other):
        if (self.priority == other.priority) and (self.item == other.item):
            return True

class PQ_UL:
    def __init__(self):
        self._queue = []
        self._len = 0

    def __len__(self):
        return self._len

    def insert(self, item, priority):
        self._queue.append(Entry(item, priority))
        self._len += 1

    def find_min(self):
        return min(self._queue)

    def remove_min(self):
        entry = min(self._queue)
        self._queue.remove(entry)
        self._len -= 1
        return entry
    
        
    
            
    

class PQ_OL:
    def __init__(self):
        self._queue = []
        self._len = 0

    def __len__(self):
        return self._len

    def insert(self, item, priority):
        self._queue.append(Entry(item, priority))
        self._len += 1
        self._queue.sort(reverse=True)

    def find_min(self):
        return self._queue[-1]

    def remove_min(self):
        self._len -= 1
        return self._queue.pop()
        
