from BSTMap import BSTMap, BSTNode # provided for you

class MyBSTMap(BSTMap):
    
    def newnode(self, key, value = None): 
        return MyBSTNode(key, value)    # overloads the `newnode` method to use the correct Node class

    # TODO: implement the three methods below
    def __eq__(self, other):
        return self.root == other.root
        

        pass #(Note that this method exists in MyBSTNode - this one should call that one)

    # the below is a "static" method
    # it belongs to the class, but does not take an instance of this class (self) as a parameter
    # note the "decorator" @staticmethod - this let's python know this is not a typical method
    @staticmethod
    def frompreorder(L):
        m = MyBSTMap()
        for i in L:
            m.put(i[0], i[1])

        return m
            
        pass

    @staticmethod
    def frompostorder(L):
        L.reverse()
        m2 = MyBSTMap()
        for i in L:
            m2.put(i[0], i[1])

        return m2
        pass

class MyBSTNode(BSTNode):
    
    newnode = MyBSTMap.newnode  # overloads the `newnode` method to use the correct Node class
    # TODO: implement the method below
    def __eq__(self, other):
        if (self is None) and (other is None):
            return True

        elif (self is None) or (other is None):
            return False

        if (self.left == other.left) and (self.right == other.right):
            return True
        
        
        pass
