
class Shape:
        def compute_area(self):
                pass
        def compute_perimeter(self):
                pass
 

class Circle(Shape):
        def __init__(self, radius):
                if radius < 0:
                        raise ValueError("radius cannot be negative")
                self.radius = radius
        def compute_area(self):
                return 3.14 * self.radius ** 2
        def compute_perimeter(self):
                return 2 * 3.14 * self.radius

class Rectangle(Shape):
        def __init__(self, width, height):
                if width < 0 or height < 0:
                        raise ValueError("width / height cannot be negative")
                self.width = width
                self.height = height
        def compute_area(self):
                return self.width * self.height
        def compute_perimeter(self):
                return 2 * (self.width + self.height)

class Triangle(Shape):
        def __init__(self, a, b, c):
                if a < 0 or b < 0 or c < 0:
                        raise ValueError("a / b / c cannot be negative")
                if not (a + b > c and a + c > b and b + c > a):
                        raise ValueError("Cannot form a triangle")
                self.a = a
                self.b = b
                self.c = c
        def compute_area(self):
                s = (self.a + self.b + self.c) / 2
                return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
        def compute_perimeter(self):
                return self.a + self.b + self.c


try:
    shapes = [Circle(3), Rectangle(2, 3), Triangle(3, 4, 5)]
    for shape in shapes:
            print("Area - "+str(shape.compute_area()))
            print("Perimeter - "+str(shape.compute_perimeter()))
except ValueError as e:
    print(e)