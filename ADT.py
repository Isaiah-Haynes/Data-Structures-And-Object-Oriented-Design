from LinkedList import LinkedList

class Stack_L:
    def __init__(self):
        self._L = list()        # Composition: the Stack_L class has a List

    def push(self, item):
        self._L.append(item)
    
    def pop(self):
        return self._L.pop()
        
        

class Stack_LL:
    def __init__(self):
        self._LL = LinkedList() # Composition: the Stack_LL class has a Linked List
    def push(self, item):
        self._LL.add_last(item)
    
    def pop(self):
        return self._LL.remove_last()

    
class Queue_L:
    def __init__(self):
        self._L = list()

    def enqueue(self, item):
        self._L.append(item)
        

    def dequeue(self):
        return self._L.pop(0)
        

class Queue_LL:
    def __init__(self):
        self._LL = LinkedList()

    def enqueue(self, item):
        self._LL.add_last(item)

    def dequeue(self):
        return self._LL.remove_first()
    
        

        pass

if __name__ == '__main__':
    ##########Test Stack_L##########
    s1 = Stack_L()
    for i in range(10): s1.push(i*3)

    for i in range(9,-1,-1): assert(s1.pop() == i*3)


    ##########Test Stack_LL#########
    s2 = Stack_LL()
    for i in range(20): s2.push(i*2)

    for i in range(19, -1, -1): assert(s2.pop() == i*2)


    ##########Test Queue_L##########
    q1 = Queue_L()
    for i in range(10): q1.enqueue(i*4)

    for i in range(10): assert(q1.dequeue() == i*4)


    ##########Test Queue_LL#########
    q2 = Queue_LL()
    for i in range(20): q2.enqueue(i*5)

    for i in range(20): assert(q2.dequeue() == i*5)

    #stack last in first out
    #queue first in first out
