"""
This module defines the abstract base class `Shape` for 2D geometric shapes.
All concrete shape classes (e.g., Rectangle, Circle, etc.) should inherit from this class and implement the area and perimeter methods.
"""
from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Abstract base class representing a generic 2D geometric shape.
    Provides interface methods for area and perimeter calculation, as well as common dunder methods.
    """
    def __init__(self, name: str):
        """
        Initialize the shape with a name.

        Args:
            name (str): The name of the shape (e.g., "Circle", "Rectangle").
        """
        self.name = name

    @abstractmethod
    def get_area(self) -> float:
        """
        Abstract method to compute the area of the shape.

        Returns:
            float: The computed area.
        """
        pass

    @abstractmethod
    def get_perimeter(self) -> float:
        """
        Abstract method to compute the perimeter of the shape.

        Returns:
            float: The computed perimeter.
        """
        pass

    def __str__(self) -> str:
        """
        Return a human-readable string representation of the shape including its name, area, and perimeter.

        Returns:
            str: A formatted string describing the shape.
        """
        return f"{self.name} (Area: {self.get_area():.2f}, Perimeter: {self.get_perimeter():.2f})"

    def __repr__(self) -> str:
        """
        Return a technical string representation of the shape instance.

        Returns:
            str: A string useful for debugging.
        """
        return f"Shape(name={self.name})"

    def __eq__(self, other) -> bool:
        """
        Compare this shape with another shape for equality based on area.

        Args:
            other (Shape): Another shape instance.

        Returns:
            bool: True if areas are equal, False otherwise.
        """
        return isinstance(other, Shape) and self.get_area() == other.get_area()

    def __lt__(self, other) -> bool:
        """
        Compare this shape with another shape based on area.

        Args:
            other (Shape): Another shape instance.

        Returns:
            bool: True if this shape's area is less than the other's, False otherwise.
        """
        return isinstance(other, Shape) and self.get_area() < other.get_area()

    def __le__(self, other) -> bool:
        """
        Compare this shape with another shape based on area for less than or equal.

        Args:
            other (Shape): Another shape instance.

        Returns:
            bool: True if this shape's area is less than or equal to the other's, False otherwise.
        """
        return self.__lt__(other) or self.__eq__(other)
