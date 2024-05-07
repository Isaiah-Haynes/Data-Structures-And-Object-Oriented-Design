from MySimulations import simulation2, simulation4, simulation5

TAPE, TQ = simulation2()
L = [0, 1, 4]
assert TAPE[:3] == L[:3]
#print(TQ.findmin()[0])
assert TQ.findmin()[0] == 10
#print(TQ.findmin()[1].multiplier)
assert TQ.findmin()[1].multiplier == 10

assert TQ.findmin()[1].multiplicity == 1
assert len(TQ) == 1

TAPE4, TQ4 = simulation4()
L4 = [2, 3, 5]
#print(str(TQ4))
assert TAPE4[:3] == L4[:3]
#print(TQ4.findmin()[0])
assert TQ4.findmin()[0] == 100
assert TQ4.findmin()[1].multiplier == 0
#print(TQ4.findmin()[1].multiplicity)
#print(len(TQ4))
assert TQ4.findmin()[1].multiplicity == 5
#print(len(TQ4))
assert len(TQ4) == 25

TAPE5, TQ5 = simulation5()
L5 = [0, 1, 4]
assert TAPE5[:3] == L5[:3]
assert TQ5.findmin()[0] == 100
assert TQ5.findmin()[1].multiplier == -1
print(TQ5.findmin()[1].multiplicity)
assert TQ5.findmin()[1].multiplicity == 5 or TQ5.findmin()[1].multiplicity == 2 or TQ5.findmin()[1].multiplicity == 10 or TQ5.findmin()[1].multiplicity == 25 or TQ5.findmin()[1].multiplicity == 50 or TQ5.findmin()[1].multiplicity == 20
assert len(TQ5) > 50
