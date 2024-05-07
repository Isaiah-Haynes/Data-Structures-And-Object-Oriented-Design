class Queue:
    def __init__(self):
        self._L = []

    def enqueue(self, item):
        self._L.append(item)

    def dequeue(self):
        return self._L.pop(0)

    def peek(self):
        return self._L[0]

    def __len__(self):
        return len(self._L)

    def isempty(self):
        return len(self) == 0

class Entry:
    def __init__(self, item, priority):
        self.priority = priority
        self.item = item
    def __lt__(self, other):
        return self.priority < other.priority
    
class HeapPQ:
    def __init__(self):
        self._entries = []
    def __len__(self):
        return len(self._entries)
    
    def insert(self, item, priority):
        self._entries.append(Entry(item, priority))
        self._upheap(len(self._entries)-1)

    def _parent(self, i):
        return (i-1) // 2

    def _children(self, i):
        left = 2*i+1
        right = 2*i+2
        return range(left, min(len(self._entries), right +1))

    def _swap(self, a,b):
        L = self._entries
        L[a], L[b] = L[b], L[a]

    def _upheap(self, i):
        L = self._entries
        parent = self._parent(i)
        if i > 0 and L[i] < L[parent]:
            self._swap(i, parent)
            self._upheap(parent)

    def findmin(self):
        return self._entries[0].item

    def removemin(self):
        L = self._entries
        item = L[0].item
        L[0] = L[-1]
        L.pop()
        self._downheap(0)
        return item

    def _downheap(self, i):
        L = self._entries
        children = self._children(i)
        if children:
            child = min(children, key = lambda x: L[x])
            if L[child] < L[i]:
                self._swap(i, child)
                self._downheap(child)

    def _heapify(self):
        n = len(self._entries)
        for i in reversed(range(n)):
            self._downheap(i)

class PriorityQueue(HeapPQ):
    def __init__(self, items=(), entries=(), key=lambda x: x):
        self._key = key
        self._entries = [Entry(i,p) for i,p in entries]
        self._entries.extend([Entry(i, key(i)) for i in items])
        self._itemmap = {entry.item : index for index,entry in enumerate(self._entries)}
        self._heapify()

    def insert(self, item, priority=None):
        if priority is None:
            priority = self._key(item)
        index = len(self._entries)
        self._entries.append(Entry(item, priority))
        self._itemmap[item] = index
        self._upheap(index)

    def _swap(self, a, b):
        L = self._entries
        va = L[a].item
        vb = L[b].item
        self._itemmap[va] = b
        self._itemmap[vb] = a
        L[a], L[b] = L[b], L[a]

    def changepriority(self, item, priority = None):
        if priority is None:
            priority = self._key(item)
        i = self._itemmap[item]
        self._entries[i].priority = priority
        self._upheap(i)
        self._downheap(i)

    def removemin(self):
        L = self._entries
        item = L[0].item
        L2 = [item]
        self._swap(0, len(L)-1)
        del self._itemmap[item]
        L.pop()
        self._downheap(0)
        return item

    def __iter__(self):
        return self
    def __next__(self):
        if len(self) > 0:
            return self.removemin()
        else: raise StopIteration
