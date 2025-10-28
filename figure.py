

class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

class Square(Shape):
    def __init__(self, width, color, filled):
        super().__init__(color, filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, width, height, color, filled):
        super().__init__(color, filled)
        self.width = width
        self.height = height

circle = Circle(radius=10, filled=True,  color="red")

print(circle.color)

print(circle.radius)

print(circle.filled)