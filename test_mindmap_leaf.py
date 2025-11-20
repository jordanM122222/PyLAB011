# Save this code in a file named: test_mindmap_leaf.py

# This line imports the class from your other file
from mindmap_leaf import MindMapLeaf

# Step 5: Create a MindMapLeaf object and test the __str__ and display methods.
print("Starting MindMapLeaf tests...")

# Create an instance with the specified name and shape
leaf = MindMapLeaf("Jean-Luc Picard", "circle")

# Test the __str__ method by printing the object directly (or using str(leaf))
print(f"Testing str(leaf): {str(leaf)}")  # Expected: ((Jean-Luc Picard))

# Test the display method with an indent of 2
print("Testing display(2):")
leaf.display(2)   # Expected:   ((Jean-Luc Picard))

print("MindMapLeaf tests completed!")
