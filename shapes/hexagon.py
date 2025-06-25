"""
This module defines the Hexagon class, representing a regular geometric hexagon.
Inherits from the Shape base class and calculates area and perimeter using side length.
"""
from shapes.shape import Shape
import math

class Hexagon(Shape):
    """
    Concrete implementation of a regular hexagon shape.

    Attributes:
        side_length (float): The length of one side of the hexagon.
    """

    def __init__(self, side_length: float):
        """
        Initialize a new Hexagon instance with the given side length.

        Args:
            side_length (float): The length of one side. Must be a positive number.

        Raises:
            ValueError: If side_length is not a positive number.
        """
        if side_length <= 0:
            raise ValueError("Side length must be a positive number.")
        super().__init__("Hexagon")
        self.side_length = side_length

    def get_area(self) -> float:
        """
        Calculate and return the area of the hexagon.

        Returns:
            float: The area of the hexagon.
        """
        return (3 * math.sqrt(3) / 2) * (self.side_length ** 2)

    def get_perimeter(self) -> float:
        """
        Calculate and return the perimeter of the hexagon.

        Returns:
            float: The perimeter of the hexagon.
        """
        return 6 * self.side_length

    def __repr__(self) -> str:
        """
        Return a technical string representation of the hexagon instance.

        Returns:
            str: A string describing the hexagon for debugging purposes.
        """
        return f"Hexagon(side_length={self.side_length})"
