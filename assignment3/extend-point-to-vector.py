import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        print(self.x == other.x and self.y == other.y)
    
    def __str__(self):
        print(f"Point({self.x}, {self.y})")
    
    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        print(math.sqrt(dx**2 + dy**2))


class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def __str__(self):
        print(f"Vector<{self.x}, {self.y}>")

    def __add__(self, other):
        v1 = self.x + other.x
        v2 = self.y + other.y
        print(f"Vector({v1}, {v2})")


# String Method for Point
point1 = Point(3, 4)
point1.__str__()

# Equality Method
point2 = Point(5, 10)
point1.__eq__(point2)

# Distance Method
point1.distance_to(point2)

# String Method for Vector
vector1 = Vector(3, 4)
vector1.__str__()

# Vector Addition
vector2 = Vector(1, 2)
vector1.__add__(vector2)
