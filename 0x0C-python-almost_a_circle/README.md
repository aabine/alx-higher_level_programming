0x0C. Python - Almost a circle
Authur : Austine Abine.

# Base Model

This project defines a base model class that serves as the foundation for other classes. It provides functionality for serialization, deserialization, file operations, and drawing shapes using the turtle module.

## Features

- JSON Serialization: The `to_json_string` method serializes a list of dictionaries to a JSON string.
- JSON Deserialization: The `from_json_string` method deserializes a JSON string to a Python list.
- Saving to File: The `save_to_file` method writes the JSON serialization of a list of objects to a file.
- Loading from File: The `load_from_file` method reads a file of JSON strings and returns a list of instantiated classes.
- CSV Serialization: The `save_to_file_csv` method writes the CSV serialization of a list of objects to a file.
- CSV Deserialization: The `load_from_file_csv` method reads a CSV file and returns a list of instantiated classes.
- Drawing Shapes: The `draw` method uses the turtle module to draw rectangles and squares.

## Usage

To use the base model, follow these steps:

1. Import the `Base` class from the module.
2. Create your own class that inherits from `Base`.
3. Implement any additional functionality specific to your class.

Here's an example of creating a Rectangle class:

```python
from base import Base

class Rectangle(Base):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
```

Now you can create instances of the Rectangle class, serialize them to JSON, save them to a file, load them from a file, and perform other operations provided by the base model.

**Dependencies**
This project requires the turtle module, which is included in the Python standard library.

# Rectangle Class

This project defines a Rectangle class that inherits from the base model class. It represents a rectangle and provides functionality for managing its attributes, calculating its area, displaying it, updating it, converting it to a dictionary, and providing string representations.

## Features

- Attribute Validation: The `width`, `height`, `x`, and `y` attributes are validated to ensure they meet the specified criteria.
- Area Calculation: The `area` method calculates and returns the area of the rectangle.
- Display: The `display` method prints the rectangle using the `#` character.
- Attribute Update: The `update` method updates the rectangle's attributes based on either positional arguments or keyword arguments.
- Dictionary Representation: The `to_dictionary` method returns a dictionary representation of the rectangle.
- String Representation: The `__str__` method provides a string representation of the rectangle for `print()` and `str()`.

## Usage

To use the Rectangle class, follow these steps:

1. Import the `Rectangle` class from the module.
2. Create an instance of the Rectangle class by providing the required arguments: `width`, `height`, and optional arguments: `x`, `y`, and `id`.
3. Access and modify the attributes of the rectangle instance as needed.
4. Use the available methods to perform operations on the rectangle.

Here's an example of using the Rectangle class:

```python
from models.rectangle import Rectangle

# Create a rectangle instance
rectangle = Rectangle(10, 5)

# Calculate and print the area
print(rectangle.area())  # Output: 50

# Display the rectangle
rectangle.display()
# Output:
# ##########
# ##########
# ##########
# ##########
# ##########

# Update the rectangle's attributes
rectangle.update(width=7, height=3, x=2, y=1)

# Convert the rectangle to a dictionary
rectangle_dict = rectangle.to_dictionary()
print(rectangle_dict)
# Output: {'id': 1, 'width': 7, 'height': 3, 'x': 2, 'y': 1}

# Get the string representation of the rectangle
print(str(rectangle))  # Output: "[Rectangle] (1) 2/1 - 7/3"
```

# Square Class

This project defines a Square class that inherits from the Rectangle class. It represents a square and provides functionality for managing its attributes, updating it, converting it to a dictionary, and providing string representations.

## Features

- Attribute Validation: The `size` attribute is validated to ensure it meets the specified criteria.
- Attribute Update: The `update` method updates the square's attributes based on either positional arguments or keyword arguments.
- Dictionary Representation: The `to_dictionary` method returns a dictionary representation of the square.
- String Representation: The `__str__` method provides a string representation of the square for `print()` and `str()`.

## Usage

To use the Square class, follow these steps:

1. Import the `Square` class from the module.
2. Create an instance of the Square class by providing the required argument: `size`, and optional arguments: `x`, `y`, and `id`.
3. Access and modify the attributes of the square instance as needed.
4. Use the available methods to perform operations on the square.

Here's an example of using the Square class:

```python
from models.square import Square

# Create a square instance
square = Square(5)

# Update the square's attributes
square.update(size=7, x=2, y=1)

# Convert the square to a dictionary
square_dict = square.to_dictionary()
print(square_dict)
# Output: {'id': 1, 'x': 2, 'y': 1, 'size': 7}

# Get the string representation of the square
print(str(square))  # Output: "[Square] (1) 2/1 - 7"
```
