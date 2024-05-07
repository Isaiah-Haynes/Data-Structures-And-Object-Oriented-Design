
class Node:
    def __init__(self, _item, _next=None):
        self._item = _item
        self._next = _next

class LinkedList:
    def __init__(self):
        self._head = None
        self._len = 0

    def add_first(self, item):
        # note the ternary (three-parameter) if:
        #    x = a if (boolean) else b
        # equiv to
        #    if (boolean): x = a
        #    else: x = b  
        self._head = Node(item) if (len(self) == 0) else Node(item, self._head)       

        self._len += 1

    def _add_last_help(self, node, item):
        #self._len += 1
        if node._next == None:
            node._next = Node(item)
            #self._len += 1
        else:
            self._add_last_help(node._next, item)
            #self._len += 1


        self._len += 1
    def add_last(self, item):
        if (len(self) == 0):
            self._head = Node(item)
            self._len += 1
        
        else:
            self._add_last_help(self._head, item) #Node(item)
            #self._len += 1

    def remove_first(self):
        if len(self) == 0: raise RuntimeError("attempt to remove_first from empty LL")

        item = self._head._item         # extract item
        self._head = self._head._next   # cut off head
        self._len -= 1                  # decrease length
        return item                     # return item



        
    def __len__(self):
        return self._len

    def __str__(self):
        if len(self) == 0: return ''                # edge case - just return an empty string

        list_of_strings = []                        # empty list to hold strings of each item
        self._str(self._head, list_of_strings)      # call helper function _str w/ head node
        return ''.join(list_of_strings)             # join all items in list_of_strings into one string

    # leading underscore - this is private!
    # attributes within this class, like __str__, can call it, but users should not
    # this is called a "helper" function
    def _str(self, node, list_of_strings):
        # base case: tail node
        if node._next is None:
            list_of_strings.append(str(node._item)) # add this item to the list of strings
            return                                  # start bouncing back up chain of recursive calls

        # non-base case: recursively call on next node
        else:
            self._str(node._next, list_of_strings)              # recursively call on next node
        
        # we have hit the tail, and are bouncing back up.
        # add this item to "list_of_strings", then return
        list_of_strings.insert(0, str(node._item) + "-")        # pre-pend "item-" to list of strings

    # TODO: recursive in
    def _contains_helper(self, node, item):
        if item == node._item:
            return True
        if node._next == None:
            return False
        else:
            return self._contains_helper(node._next, item)
        
    def __contains__(self, item):
        return self._contains_helper(self._head, item)
    # TODO: recursive add_last


if __name__ == '__main__':
    # Test Node
    n = Node(1)
    assert n._item == 1
    assert n._next is None
    print("Node tests pass")

    # Test LL - add_first/len/remove_first
    LL = LinkedList()
    
    for i in range(4):
        assert len(LL) == i
        LL.add_first(i)
    
    for i in range(4):
        assert LL.remove_first() == 3-i
        assert len(LL) == 3-i

    # Test LL - str
    for i in range(4): LL.add_first(i)
    assert str(LL) == "3-2-1-0"
    print("starter LL tests pass!")

    # TODO:
    #   * test in
    #   * test add_last

    LL1 = LinkedList()
    
    for i in range(10):
        assert len(LL1) == i
        LL1.add_first(i)
    assert 3 in LL1
    print("Magic Method 'in' pass!!")

    LL2 = LinkedList()
    for i in range(4):
        LL2.add_last(i)
    assert str(LL2) == '0-1-2-3'
    #print(len(LL2))

    print("add_last function pass!!")

