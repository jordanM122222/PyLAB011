# mindmap_composite.py
import os

class MindMapComposite:
    """
    Represents a composite node in a mind map, capable of having children (other
    composite nodes or leaf nodes).
    """

    def __init__(self, name, shape):
        self.name = name
        self.shape = shape
        self.children = []

    def add(self, child):
        """Adds a child node to this composite node."""
        self.children.append(child)

    def remove(self, child):
        """Removes a child node from this composite node."""
        if child in self.children:
            self.children.remove(child)

    def __str__(self):
        """Returns a string representation of the node name formatted with its shape."""
        return self.get_shape_representation().format(self.name)

    def display(self, indent=0):
        """Prints the node and all its children with appropriate indentation."""
        print(" " * indent + str(self))
        for child in self.children:
            child.display(indent + 2)

    def get_shape_representation(self):
        """Returns the shape template string from a dictionary."""
        shapes = {
            "box": "[ {} ]",
            "circle": "( {} )",
            "diamond": "< {} >",
            "square": "[ {} ]", # Added square for test compatibility
            "cloud": "~( {} )~", # Added cloud for test compatibility
            "none": "{}"
        }
        return shapes.get(self.shape, "{}")

