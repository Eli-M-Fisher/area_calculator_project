from shapes.rectangle import Rectangle

class Triangle(Rectangle):
    def __init__(self, base: float, height: float):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        super().__init__(width=base, height=height)
        self.name = "Triangle"

    def get_area(self) -> float:
        return 0.5 * self.width * self.height

    def __repr__(self) -> str:
        return f"Triangle(base={self.width}, height={self.height})"
