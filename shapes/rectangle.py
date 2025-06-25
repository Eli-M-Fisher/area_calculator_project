from shapes.shape import Shape

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers.")
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def get_area(self) -> float:
        return self.width * self.height

    def get_perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"
