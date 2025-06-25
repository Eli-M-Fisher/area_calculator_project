"""
This module defines the Triangle class, representing a geometric triangle.
Inherits from the Rectangle class and overrides the area calculation.
"""
from shapes.rectangle import Rectangle

class Triangle(Rectangle):
    """
    Concrete implementation of a triangle shape.

    A triangle is represented using a base and height, and its area is calculated as half that of the surrounding rectangle.

    Attributes:
        base (float): The length of the base of the triangle.
        height (float): The height of the triangle.
    """
    def __init__(self, base: float, height: float):
        """
        Initialize a new Triangle instance with a base and height.

        Args:
            base (float): The length of the triangle's base. Must be positive.
            height (float): The height of the triangle. Must be positive.

        Raises:
            ValueError: If base or height is not a positive number.
        """
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        super().__init__(width=base, height=height)
        self.name = "Triangle"

    def get_area(self) -> float:
        """
        Calculate and return the area of the triangle.

        Returns:
            float: The area of the triangle.
        """
        return 0.5 * self.width * self.height

    def __repr__(self) -> str:
        """
        Return a technical string representation of the triangle instance.

        Returns:
            str: A string describing the triangle for debugging purposes.
        """
        return f"Triangle(base={self.width}, height={self.height})"
