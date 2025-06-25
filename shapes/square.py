"""
This module defines the Square class, representing a geometric square.
Inherits from the Rectangle class and ensures both sides are equal.
"""

from shapes.rectangle import Rectangle

class Square(Rectangle):
    """
    Concrete implementation of a square shape.

    A square is a special case of a rectangle where all sides are equal.

    Attributes:
        side_length (float): The length of each side of the square.
    """
    def __init__(self, side_length: float):
        """
        Initialize a new Square instance with equal side lengths.

        Args:
            side_length (float): The length of each side of the square. Must be positive.

        Raises:
            ValueError: If side_length is not a positive number.
        """
        if side_length <= 0:
            raise ValueError("Side length must be a positive number.")
        super().__init__(width=side_length, height=side_length)
        self.name = "Square"

    def __repr__(self) -> str:
        """
        Return a technical string representation of the square instance.

        Returns:
            str: A string describing the square for debugging purposes.
        """
        return f"Square(side_length={self.width})"
