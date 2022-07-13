# initially we have a Point that we want to initialise , and riginally they are cartesian coordinates
# but maybe the cordinates are in polar
# the problems are illustrated in the code

# 1> first we can define a staticmethod to explicitly say what we need to create and how
# 2> we can create a Factory class; when we have many factory methods it makes sense to group them in a class
# factory is a sparate entity

from enum import Enum
from math import *


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    # def __init__(self, x, y):
    #     self.x = x
    #     self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    # redeclaration won't work
    # def __init__(self, rho, theta):

    # Problem: how to map every time that a and b is the cartesian x and y or the polar x an dy
    def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
        if system == CoordinateSystem.CARTESIAN:
            self.x = a
            self.y = b
        elif system == CoordinateSystem.POLAR:
            self.x = a * sin(b)
            self.y = a * cos(b)

        # Problem : how to add a new system -> steps to add a new system
        # 1. augment CoordinateSystem
        # 2. change init method --> it can become a god object
        # this would also break the Open Closed Principle


    #1> this is a factory method; better naming and convenient way to create objects
    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    #1> this is a factory method; better naming and convenient way to create objects
    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * sin(theta), rho * cos(theta))


    # this used to discover that there is a factory that the user can use
    class Factory:
        @staticmethod
        def new_cartesian_point(x, y):
            return Point(x, y)

    # this way we can make an instace of the factory
    factory = Factory()

# 2>  take out factory methods to a separate class
class PointFactory:
    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * sin(theta), rho * cos(theta))


if __name__ == '__main__':
    p1 = Point(2, 3, CoordinateSystem.CARTESIAN)
    p2 = PointFactory.new_cartesian_point(1, 2)
    # or you can expose factory through the type
    p3 = Point.Factory.new_cartesian_point(5, 6)
    p4 = Point.factory.new_cartesian_point(7, 8) # singleton instance
    print(p1, p2, p3, p4)
