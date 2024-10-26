class Node:
    def __init__(self, value):
        self.value = value  # Value of the node
        self.left = None    # Left child (another Node)
        self.right = None   # Right child (another Node)


def build_binary_tree():
    # Level 0 (Root)
    root = Node(1)

    # Level 1
    root.left = Node(2)
    root.right = Node(3)

    # Level 2
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    # Level 3
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(10)
    root.left.right.right = Node(11)
    root.right.left.left = Node(12)
    root.right.left.right = Node(13)
    root.right.right.left = Node(14)
    root.right.right.right = Node(15)

    return root


# Preorder traversal of the tree (root, left, right)
def preorder_traversal(node):
    if node is not None:
        print(node.value, end=" ")  # Print the current node's value
        preorder_traversal(node.left)  # Traverse the left subtree
        preorder_traversal(node.right)  # Traverse the right subtree


# Postorder traversal of the tree (left, right, root)
def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)  # Traverse the left subtree
        postorder_traversal(node.right)  # Traverse the right subtree
        print(node.value, end=" ")  # Print the current node's value


# Build the tree and perform traversals
root = build_binary_tree()

print("Preorder traversal of the binary tree:")
preorder_traversal(root)

print("\nPostorder traversal of the binary tree:")
postorder_traversal(root)
