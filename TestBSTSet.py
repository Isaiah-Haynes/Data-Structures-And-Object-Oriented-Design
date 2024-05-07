from BSTSet import BSTSet


bst = BSTSet()

for i in [12, 49, 13, 5, 42]:
  bst.put(i)

preo = []
for j in bst.pre_order():
  preo.append(j)
bst.__repr__()
print(preo)
preo2 = []
for k in bst.pre_order():
  preo2.append(k)

print(preo2)


