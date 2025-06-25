from shapes.rectangle import Rectangle
from shapes.square import Square
from shapes.triangle import Triangle
from shapes.circle import Circle
from shapes.hexagon import Hexagon

def get_positive_number(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Please enter a positive number.")

def main():
    print("<[*][*][*]> Area Shape Resolver Calculator <[*][*][*]>")
    print("Available shapes: rectangle, square, triangle, circle, hexagon")
    shape_type = input("Enter the shape type: ").strip().lower()

    shape = None

    if shape_type == "rectangle":
        width = get_positive_number("Enter width: ")
        height = get_positive_number("Enter height: ")
        shape = Rectangle(width, height)

    elif shape_type == "square":
        side = get_positive_number("Enter side length: ")
        shape = Square(side)

    elif shape_type == "triangle":
        base = get_positive_number("Enter base: ")
        height = get_positive_number("Enter height: ")
        shape = Triangle(base, height)

    elif shape_type == "circle":
        radius = get_positive_number("Enter radius: ")
        shape = Circle(radius)

    elif shape_type == "hexagon":
        side = get_positive_number("Enter side length: ")
        shape = Hexagon(side)

    else:
        print("Unsupported shape type.")
        return

    print("\nResult:")
    print(shape)

if __name__ == "__main__":
    main()