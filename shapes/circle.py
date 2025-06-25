"""
This module defines the Circle class, representing a geometric circle.
Inherits from the Shape base class and implements specific area and perimeter calculations using the radius.
"""
from shapes.shape import Shape
import math

class Circle(Shape):
    """
    Concrete implementation of a circle shape.

    Attributes:
        radius (float): The radius of the circle.
    """
    def __init__(self, radius: float):
        """
        Initialize a new Circle instance with the given radius.

        Args:
            radius (float): The radius of the circle. Must be a positive number.

        Raises:
            ValueError: If radius is not a positive number.
        """
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        super().__init__("Circle")
        self.radius = radius

    def get_area(self) -> float:
        """
        Calculate and return the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def get_perimeter(self) -> float:
        """
        Calculate and return the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.radius

    def __repr__(self) -> str:
        """
        Return a technical string representation of the circle instance.

        Returns:
            str: A string describing the circle for debugging purposes.
        """
        return f"Circle(radius={self.radius})"
