from shapes.rectangle import Rectangle
from shapes.square import Square
from shapes.triangle import Triangle
from shapes.circle import Circle
from shapes.hexagon import Hexagon

def get_positive_number(prompt: str) -> float:
    while True:
        try:
            value = input(prompt).strip()
            if not value:
                print("Input cannot be empty.")
                continue
            number = float(value)
            if number <= 0:
                print("Value must be a positive number.")
                continue
            return number
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def create_shape(shape_type: str):
    shape_type = shape_type.strip().lower()

    if shape_type == "rectangle":
        width = get_positive_number("Enter width: ")
        height = get_positive_number("Enter height: ")
        return Rectangle(width, height)

    elif shape_type == "square":
        side = get_positive_number("Enter side length: ")
        return Square(side)

    elif shape_type == "triangle":
        base = get_positive_number("Enter base: ")
        height = get_positive_number("Enter height: ")
        return Triangle(base, height)

    elif shape_type == "circle":
        radius = get_positive_number("Enter radius: ")
        return Circle(radius)

    elif shape_type == "hexagon":
        side = get_positive_number("Enter side length: ")
        return Hexagon(side)

    else:
        print("Unsupported shape type. Please choose from: rectangle, square, triangle, circle, hexagon.")
        return None

def main():
    print("=== Area Shape Resolver Calculator ===")
    print("Available shapes: rectangle, square, triangle, circle, hexagon")

    try:
        while True:
            shape_type = input("\nEnter the shape type (or 'exit' to quit): ").strip().lower()
            if shape_type == "exit":
                print("Goodbye!")
                break

            if not shape_type:
                print("Please enter a shape type.")
                continue

            shape = create_shape(shape_type)
            if shape:
                print("\nResult:")
                print(shape)

    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Exiting...")

if __name__ == "__main__":
    main()
