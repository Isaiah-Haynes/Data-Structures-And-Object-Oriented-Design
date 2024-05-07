class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pass
    def dist_from_origin(self):
        distance = (self.x**2 + self.y**2)**.5
        return distance
        pass
    def __eq__(self, other):
        if (self.x == other.x) and (self.y == other.y):
            return True
        elif self.dist_from_origin() == other.dist_from_origin():
            return True
        else:
            return False
        pass
    def __lt__(self, other):
        if self.dist_from_origin() < other.dist_from_origin():
            return True
        else:
            return False
        pass
    def __gt__(self, other):
        if self.dist_from_origin() > other.dist_from_origin():
            return True
        else:
            return False
        pass
        
    def __str__(self):
        return "Point({}, {})".format(self.x, self.y)
        pass
        
if __name__ == '__main__':
    p1 = Point(3, 4)
    p2 = Point(0, 6)
    p3 = Point(3, 4)
    p4 = Point(6, 0)
    p5 = Point(3, 4)
    p6 = Point(4, 3)
    assert p1.x == 3
    assert p1.y == 4
    assert p1.dist_from_origin() == 5
    assert p2.dist_from_origin() == 6
    assert p1.__str__() == "Point(3, 4)"
    assert p1 < p2
    assert (p2 < p1) #== False
    assert p2 > p1
    assert (p1 > p2) #== False
    assert p3 == p1
    assert (p1 == p2) #== False
    assert p2.dist_from_origin() == p4.dist_from_origin()
    assert (p5 == p6) #== True
