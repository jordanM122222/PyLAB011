import os  # Although 'os' isn't used in this specific class logic, it's included as requested.


class MindMapComposite:
    """
    Represents a composite node in a mind map, capable of having children (other
    composite nodes or leaf nodes).
    """

    # Step 1: Write the __init__ method
    # - Define an __init__ method that takes name and shape as parameters.
    # - Initialize self.name, self.shape, and an empty list self.children.
    def __init__(self, name, shape):
        self.name = name
        self.shape = shape
        # Hint: Use self.children = [] to initialize the list.
        self.children = []

    # Step 2: Write the add and remove methods
    # - Use append() to add and remove() to delete from the children list.
    def add(self, child):
        """Adds a child node to this composite node."""
        # HINT: the child parameter is an object of type MindMapComposite or MindMapLeaf
        self.children.append(child)

    def remove(self, child):
        """Removes a child node from this composite node."""
        if child in self.children:
            self.children.remove(child)

    # Step 3: Write the __str__ method
    # - Format the name using get_shape_representation() and return it.
    def __str__(self):
        """Returns a string representation of the node name formatted with its shape."""
        # Format self.name using get_shape_representation() and return the string.
        return self.get_shape_representation().format(self.name)

    # Step 4: Write the display method
    # - Print the name with the specified indentation.
    # - Loop over each child and call display with increased indentation.
    def display(self, indent=0):
        """Prints the node and all its children with appropriate indentation."""
        # Print the composite’s name with the specified indentation.
        print(" " * indent + str(self))
        # Use a loop to call child.display(indent + 2) for each child.
        for child in self.children:
            child.display(indent + 2)

    # Step 5: Write the get_shape_representation method
    # - Create a dictionary with shape templates.
    # - Use shapes.get to return the template.
    def get_shape_representation(self):
        """Returns the shape template string from a dictionary."""
        # HINT: This is the SAME as MindMapLeaf!
        shapes = {
            "box": "[ {} ]",
            "circle": "( {} )",
            "diamond": "< {} >",
            "none": "{} "
        }
        # Define a dictionary with shape templates and return the template using shapes.get().
        # Uses a default value if the shape key is not found.
        return shapes.get(self.shape, "{}")


# Example Usage (optional, for testing the class structure):
# Note: This requires a 'MindMapLeaf' class to fully function in a real scenario,
# but demonstrates how the composite class works.
if __name__ == '__main__':
    # Assuming a MindMapLeaf class exists with the same display/str methods
    # class MindMapLeaf: ...

    # root = MindMapComposite("Root Node", "box")
    # child1 = MindMapComposite("Child 1", "circle")
    # child2 = MindMapLeaf("Leaf 1", "none")

    # root.add(child1)
    # root.add(child2)

    # root.display()
    pass