import copy
from unittest import TestCase

class DeeperPoint:
    def __init__(self, deep = 0):
        self.deep = deep

class Point:
    def __init__(self, x=0, y=0, detail = DeeperPoint()
    ):
        self.x = x
        self.y = y
        self.detail = detail
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.detail.deep})"

class Line:
    def __init__(self, start = Point(), end=Point()):
        self.start = start
        self.end = end
    
    def __str__(self):
        return f"{self.start} to {self.end}"

    def shallow_copy(self):
        """
        this will lead to a change in the original object
        if you touch the x or y of a point
        """
        start_point = self.start
        end_point = self.end
        return Line(start_point, end_point)

    def deep_copy(self):
        """
        this will not lead to a change in the original object
        if you touch the x or y of a point becuase it goes to a deeper level
        
        with the same logic if there was another level of the point this would change
        this would go on and on and we would need a function deep_deep copy
        
        To tackle this issue we would need a recursive function which is what copy.deepcopy does
        """
        start_point = Point(self.start.x, self.start.y)
        end_point = Point(self.end.x, self.end.y)
        return Line(start_point, end_point)

    def deep_deep_copy(self):
        start_point = Point(self.start.x, self.start.y, self.start.detail)
        end_point = Point(self.end.x, self.end.y, self.end.detail)
        return Line(start_point, end_point)



l1 = Line(Point(1,2, DeeperPoint(1.2)), Point(3,4,DeeperPoint(3.4)))

# this does not change the original object
l2 = l1.deep_deep_copy()
l2.end.y = 6


print("deep copy")
print(f"{l1}: l1")
print(f"{l2}: l2")


# this changes also the reference to l1


l11 = Line(Point(11,22), Point(33,44, DeeperPoint('heloo')))
l11_deep_deep_copy = l11.deep_deep_copy()
# this does not change because the end is a point which has been copied
l12 = l11.shallow_copy()
l12.end = Point(88,99)

# this changes also the reference to l11 because start.y is an object reference
l13 = l11.shallow_copy()
l13.start.y = 10


print(f"original l11: {l11_deep_deep_copy}")
#
print("shallow copy that does not change")
print(f"{l11}: l11")
print(f"{l12}: l12")
# this changes the reference to l11 for the print before so you need to uncomment it in order to see the resultes before
print("shallow copy that changes, but it will change also the previous that I say it does not change")
print(f"{l11}: l11")
print(f"{l13}: l13")
