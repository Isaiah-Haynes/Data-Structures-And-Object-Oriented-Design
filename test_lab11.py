#!NO_IMPORT
from lab11 import Graph_ES, Graph_AS
# a <==> b
# ^      ^
# |      |
# ∨      ∨
# c <==> d
def nbr_check(g, v, nbrs):
  #print("v = {}".format(v))
  check = set()
  for n in g._neighbors(v):
    check.add(n)
  assert check == nbrs

g = Graph_AS({'a', 'b', 'c', 'd'})
g.add_edge(('a', 'c'))
nbr_check(g, 'a', {'c'})
g.add_edge(('a', 'b'))
print(g._neighbors('a'))
nbr_check(g, 'a', {'c', 'b'})
g.remove_edge(('a', 'c'))
nbr_check(g, 'a', {'b'})
es = {('b', 'a'), ('b', 'd'),
      ('c', 'a'), ('c', 'd'),
      ('d', 'b'), ('d', 'c')}
      
for e in es: g.add_edge(e)
nbr_check(g, 'b', {'a', 'd'})
nbr_check(g, 'c', {'a', 'd'})
nbr_check(g, 'd', {'c', 'b'})
try:
  g.remove_edge(('a', 'c'))
  raise AssertionError
except KeyError:
  pass
