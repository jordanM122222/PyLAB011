class MindMapLeaf:
    # Step 1: Write the __init__ method
    def __init__(self, name, shape):
        self.name = name
        self.shape = shape

    # Step 2: Write the __str__ method
    def __str__(self):
        # This calls the get_shape_representation method and formats the name into it
        shape_representation = self.get_shape_representation()
        return shape_representation.format(self.name)

    # Step 3: Write the display method
    def display(self, indent=0):
        indent_str = " " * indent
        print(indent_str + str(self))

    # Step 4: Write the get_shape_representation method
    # - Create a shapes dictionary with shape templates.
    # - Use shapes.get to return the appropriate shape template.
    def get_shape_representation(self):
        shapes = {
            "circle": "(( {} ))",
            "oval": "( {} )",
            "square": "[ {} ]",
            "cloud": "){}(",
            "hexagon": "{{{{ {} }}}}",
            "bang": ")){}<<"  # Adjusted 'bang' template for clarity
        }
        # Return the template or a default "{}" if the shape key isn't found
        return shapes.get(self.shape, "{}")


# ================================================
# Example Usage to test all methods:
# ================================================
if __name__ == "__main__":
    print("--- Testing MindMapLeaf Class with new shapes ---")

    # Create instances using the new shapes
    topic_1 = MindMapLeaf(name="Circle Topic", shape="circle")
    topic_2 = MindMapLeaf(name="Square Topic", shape="square")
    topic_3 = MindMapLeaf(name="Unknown Shape", shape="triangle")
    topic_4 = MindMapLeaf(name="Hexagon Topic", shape="hexagon")

    # Display them
    topic_1.display()
    topic_2.display(indent=4)
    topic_3.display(indent=8)
    topic_4.display(indent=4)

    print("\n--- Code execution finished ---")



