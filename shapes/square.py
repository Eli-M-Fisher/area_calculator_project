from shapes.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side_length: float):
        if side_length <= 0:
            raise ValueError("Side length must be a positive number.")
        super().__init__(width=side_length, height=side_length)
        self.name = "Square"

    def __repr__(self) -> str:
        return f"Square(side_length={self.width})"
