from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_area(self) -> float:
        pass

    @abstractmethod
    def get_perimeter(self) -> float:
        pass

    def __str__(self) -> str:
        return f"{self.name} (Area: {self.get_area():.2f}, Perimeter: {self.get_perimeter():.2f})"

    def __repr__(self) -> str:
        return f"Shape(name={self.name})"

    def __eq__(self, other) -> bool:
        return isinstance(other, Shape) and self.get_area() == other.get_area()

    def __lt__(self, other) -> bool:
        return isinstance(other, Shape) and self.get_area() < other.get_area()

    def __le__(self, other) -> bool:
        return self.__lt__(other) or self.__eq__(other)
