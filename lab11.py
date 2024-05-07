class Graph_ES:
    def __init__(self, vertices=(), edges=()):
        self._v = set()
        self._e = set()
        self._len = 0
        for v in vertices: self.add_vertex(v)
        for u,v in edges: self.add_edge((u,v))
    def __len__(self):
        return self._len

    def __iter__(self):
        return (v for v in self._v)
    def add_vertex(self, v):
        self._v.add(v)
        self._len += 1

    def remove_vertex(self, v):
        if v not in self._v:
            raise KeyError
        self._v.remove(v)
        self._len-=1

    def add_edge(self, e):
        self._e.add(e)

    def remove_edge(self, e):
        if e not in self._e:
            raise KeyError
        self._e.remove(e)

    def _neighbors(self, v):
        return (p for u,p in self._e if u == v)

class Graph_AS:
    def __init__(self, vertices = (), edges = ()):
        self._v = set()
        self._nbrs = {}
        self._len = 0
        for v in vertices: self.add_vertex(v)
        for e in edges: self.add_edge(e)
    def __len__(self):
        return self._len

    def __iter__(self):
        return (v for v in self._v)
    
    def add_vertex(self, v):
        self._v.add(v)
        self._len+=1

    def remove_vertex(self, v):
        if v not in self._v:
            raise KeyError
        self._v.remove(v)
        self._len-=1

    def add_edge(self, e):
        #this replaces previous value with a new value
        #self._nbrs[e[0]] = [e[1]]
        if e[0] not in self._nbrs:
            self._nbrs[e[0]] = list()
        self._nbrs[e[0]].extend(e[1])

    def remove_edge(self, e):
        if e[0] not in self._nbrs:
            raise KeyError
        self._nbrs[e[0]].remove(e[1])

    def _neighbors(self, v):
        return (i for i in self._nbrs[v])

        
