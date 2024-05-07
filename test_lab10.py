from lab10 import Entry, PQ_UL, PQ_OL
pq = PQ_OL()
n = 100
for i in range(n):
    assert len(pq) == i
    pq.insert(str(i), i)
old = pq.remove_min()
for i in range(1, n):
    peak = pq.find_min()
    new = pq.remove_min()
    assert new == peak
    assert old.priority <= new.priority
    assert len(pq) == n - i - 1
    old = new
