# TODO: Add a class Graph
from ADTS import Queue, PriorityQueue as PQ
class Graph:
    def __init__(self, V=(), E=()):
        raise NotImplementedError
    def add_vertex(self, v):
        raise NotImplementedError
    def remove_vertex(self, v):
        raise NotImplementedError
    def add_edge(self, u, v, w=1):
        raise NotImplementedError
    def remove_edge(self, u, v, w=1):
        raise NotImplementedError
    def neighbors(self, v):
        raise NotImplementedError
    def weight(self, u, v, w=None):
        raise NotImplementedError
    def bfs(self, v):
        tree = {}
        tovisit = Queue()
        tovisit.enqueue((None, v))
        while tovisit:
            a,b = tovisit.dequeue()
            if b not in tree:
                tree[b] = a
                for n in self.neighbors(b):
                    tovisit.enqueue((b,n))
        return tree
        pass

    def dfs(self, v):
        tree = {}
        tovisit = [(None, v)]
        while tovisit:
            a,b = tovisit.pop()
            if b not in tree:
                tree[b] = a
                for n in self.neighbors(b):
                    tovisit.append((b,n))
        return tree
        pass

    def dijkstra(self, v):
        tree = {}
        D = {v: 0}
        tovisit = PQ()
        tovisit.insert((None,v),0)
        for a,b in tovisit:
            if b not in tree:
                tree[b] = a
                if a is not None:
                    D[b] = D[a] + self.weight(a,b)
                for n in self.neighbors(b):
                    tovisit.insert((b,n), D[b] + self.weight(b,n))
        
        return tree, D

    def primm(self, v):
        tree = {}
        tovisit = PQ()
        tovisit.insert((None, v),0)
        for a, b in tovisit:
            if b not in tree:
                tree[b] = a
                for n in self.neighbors(b):
                    tovisit.insert((b,n), self.weight(b,n))
        return tree
        pass

# TODO: Add a class for AdjacencySetGraph that inherits from Graph
class AdjacencySetGraph(Graph):
    def __init__(self, vertices = (), edges = ()):
        self._v = set()
        self._ngbrs = {}
        for v in vertices: self.add_vertex(v)
        for e in edges: self.add_edge(*e)
        
    def add_vertex(self, v):
        self._v.add(v)
        self._ngbrs[v] = {}

    def remove_vertex(self, v):
        self._v.remove(v)
        del self._ngbrs[v]

    def add_edge(self, u, v, w=None):
        self._ngbrs[u][v] = w
        self._ngbrs[v][u] = w
    def remove_edge(self, u, v, w=None):
        del self._ngbrs[u][v]
        del self._ngbrs[v][u]

    def neighbors(self, v):
        return self._ngbrs[v]

    def weight(self, u, v):
        return self._ngbrs[u][v]
    
# TODO: Add a class for EdgeSetGraph that inherits from Graph
class EdgeSetGraph(Graph):
    def __init__(self, vertices=(), edges=()):
        self._v = set()
        self._e = set()
        for v in vertices: self.add_vertex(v)
        #for u,v in edges: self.add_edge(u,v)
        for e in edges: self.add_edge(*e)

    def add_vertex(self, v):
        self._v.add(v)

    def remove_vertex(self, v):
        self._v.remove(v)
        for edge in self._e:
            if edge[1] == v:
                self.remove_edge(edge[0], edge[1])

    def add_edge(self, u, v, w=None):
        self._e.add((u,v,w))
        self._e.add((v,u,w))

    def remove_edge(u, v, w=None):
        self._e.remove(u, v, w)
        self._e.remove(v,u,w)

    def neighbors(self, v):
        return (p for u,p,w in self._e if u == v)

    def weight(self, u, v):
        for a,b,c in self._e:
            if (a==u) and (b==v):
                return c
        pass



        
