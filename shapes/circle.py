from shapes.shape import Shape
import math

class Circle(Shape):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        super().__init__("Circle")
        self.radius = radius

    def get_area(self) -> float:
        return math.pi * (self.radius ** 2)

    def get_perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def __repr__(self) -> str:
        return f"Circle(radius={self.radius})"
