# Define the structure of a Node
class Node:
    def init(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to insert a node into the binary tree
def insert_node(root, data):
    if root is None:
        return Node(data)
    elif data < root.data:
        root.left = insert_node(root.left, data)
    else:
        root.right = insert_node(root.right, data)
    return root

# In-order traversal of the binary tree
def in_order_traversal(root):
    if root is not None:
        in_order_traversal(root.left)
        print(root.data, end=" ")
        in_order_traversal(root.right)

# Main function
if name == "main":
    root = None

    # Insert nodes into the binary tree
    root = insert_node(root, 50)
    root = insert_node(root, 30)
    root = insert_node(root, 70)
    root = insert_node(root, 20)
    root = insert_node(root, 40)
    root = insert_node(root, 60)
    root = insert_node(root, 80)

    # Print the in-order traversal
    print("In-order Traversal:", end=" ")
    in_order_traversal(root)
    print()