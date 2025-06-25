from shapes.shape import Shape
import math

class Hexagon(Shape):
    def __init__(self, side_length: float):
        if side_length <= 0:
            raise ValueError("Side length must be a positive number.")
        super().__init__("Hexagon")
        self.side_length = side_length

    def get_area(self) -> float:
        return (3 * math.sqrt(3) / 2) * (self.side_length ** 2)

    def get_perimeter(self) -> float:
        return 6 * self.side_length

    def __repr__(self) -> str:
        return f"Hexagon(side_length={self.side_length})"
