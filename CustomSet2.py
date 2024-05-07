from CustomSet import CustomSet
cs = CustomSet()
n = 10
for i in range(n):
    assert not i in cs
    cs.add(i)
    assert i in cs
    
chars="abcdefghijklmnopqrstuvwxyz"
cs = CustomSet()
for c in chars:
  assert not c in cs
  cs.add(c)
  assert c in cs
  
cs = CustomSet()
bs = set()
import random
random.seed(2050)
n = 100000
for i in range(n):
    new = random.randint(0,n)
    bs.add(new)
    cs.add(new)
    assert new in cs
    
for i in range(50000):
  assert not "a" in cs

cs2 = CustomSet()
for i in range(100):
    cs2.add(i)
cs2.remove(3)
