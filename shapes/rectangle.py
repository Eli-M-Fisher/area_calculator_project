"""
This module defines the Rectangle class, representing a geometric rectangle.
Inherits from the abstract base class Shape and implements area and perimeter calculations.
"""
from shapes.shape import Shape

class Rectangle(Shape):
    """
    Concrete implementation of a rectangle shape.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """
    def __init__(self, width: float, height: float):
        """
        Initialize a new Rectangle instance with the specified width and height.

        Args:
            width (float): The width of the rectangle. Must be positive.
            height (float): The height of the rectangle. Must be positive.

        Raises:
            ValueError: If either dimension is not a positive number.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers.")
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def get_area(self) -> float:
        """
        Calculate and return the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

    def get_perimeter(self) -> float:
        """
        Calculate and return the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

    def __repr__(self) -> str:
        """
        Return a technical string representation of the rectangle instance.

        Returns:
            str: A string describing the rectangle for debugging purposes.
        """
        return f"Rectangle(width={self.width}, height={self.height})"
