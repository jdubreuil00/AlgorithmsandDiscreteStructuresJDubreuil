class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Traversing the binary tree
def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.value)
        inorder_traversal(node.right)

def print_adjacency_matrix(root):
    # Calculate the height of the binary tree
    def calculate_height(node):
        if node is None:
            return 0
        return max(calculate_height(node.left), calculate_height(node.right)) + 1

    # Create an empty adjacency matrix
    height = calculate_height(root)
    matrix = [[0] * (2 ** height - 1) for _ in range(height)]

    # Populate the adjacency matrix recursively
    def populate_matrix(node, level, position):
        if node is not None:
            matrix[level][position] = 1
            populate_matrix(node.left, level + 1, position * 2)
            populate_matrix(node.right, level + 1, position * 2 + 1)

    populate_matrix(root, 0, 0)

    # Print the adjacency matrix
    for row in matrix:
        print(row)

# Create the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Adjacency Matrix:")
print_adjacency_matrix(root)
