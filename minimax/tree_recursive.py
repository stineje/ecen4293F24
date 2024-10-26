class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_binary_tree(current_depth, max_depth, current_value=1):
    """ Recursive function to build a binary tree of any depth """
    if current_depth > max_depth:
        return None

    # Create the current node
    node = Node(current_value)

    # Recursively create left and right children, increasing the current depth and value
    node.left = build_binary_tree(
        current_depth + 1, max_depth, current_value * 2)
    node.right = build_binary_tree(
        current_depth + 1, max_depth, current_value * 2 + 1)

    return node


def postorder_traversal(node):
    """ Postorder traversal of the tree (left, right, root) """
    if node is not None:
        postorder_traversal(node.left)  # Traverse the left subtree
        postorder_traversal(node.right)  # Traverse the right subtree
        print(node.value, end=" ")  # Print the current node's value


def preorder_traversal(node):
    """ Preorder traversal of the tree (root, left, right """
    if node is not None:
        print(node.value, end=" ")  # Print the current node's value
        preorder_traversal(node.left)  # Traverse the left subtree
        preorder_traversal(node.right)  # Traverse the right subtree


# Input: desired depth of the tree
desired_depth = int(4)

# Build the tree
root = build_binary_tree(1, desired_depth)

# Preorder traversal of the tree
print("Preorder traversal of the binary tree:")
preorder_traversal(root)
print()

# Postorder traversal of the tree
print("Postorder traversal of the binary tree:")
postorder_traversal(root)
