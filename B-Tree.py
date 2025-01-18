class BTreeNode:
    def __init__(self, t, is_leaf=True):
        self.t = t  # Minimum degree (defines the range for the number of keys)
        self.keys = []  # List to store keys
        self.children = []  # List to store child pointers
        self.is_leaf = is_leaf  # True if the node is a leaf node

    def insert_non_full(self, key):
        i = len(self.keys) - 1

        if self.is_leaf:  # If the node is a leaf
            self.keys.append(None)  # Add space for the new key
            while i >= 0 and key < self.keys[i]:
                self.keys[i + 1] = self.keys[i]  # Shift keys to the right
                i -= 1
            self.keys[i + 1] = key  # Insert the new key
        else:  # If the node is not a leaf
            while i >= 0 and key < self.keys[i]:
                i -= 1
            i += 1  # Get the child index
            if len(self.children[i].keys) == 2 * self.t - 1:  # If the child is full
                self.split_child(i)
                if key > self.keys[i]:
                    i += 1
            self.children[i].insert_non_full(key)

    def split_child(self, i):
        t = self.t
        y = self.children[i]  # Full child to split
        z = BTreeNode(t, y.is_leaf)  # New node to store (t-1) keys of y

        # Move (t-1) keys from y to z
        z.keys = y.keys[t:(2 * t - 1)]
        y.keys = y.keys[:t - 1]

        # If y is not a leaf, move (t) children from y to z
        if not y.is_leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]

        self.children.insert(i + 1, z)  # Add z as a child of this node
        self.keys.insert(i, y.keys.pop())  # Move the middle key of y to this node

    def traverse(self):
        for i in range(len(self.keys)):
            if not self.is_leaf:
                self.children[i].traverse()
            print(self.keys[i], end=" ")
        if not self.is_leaf:
            self.children[-1].traverse()

    def search(self, key):
        i = 0
        while i < len(self.keys) and key > self.keys[i]:
            i += 1

        if i < len(self.keys) and self.keys[i] == key:
            return True

        if self.is_leaf:
            return False
        return self.children[i].search(key)


class BTree:
    def __init__(self, t):
        self.t = t  # Minimum degree
        self.root = BTreeNode(t)

    def insert(self, key):
        root = self.root
        if len(root.keys) == 2 * self.t - 1:  # If root is full
            s = BTreeNode(self.t, False)  # Create a new root
            s.children.append(self.root)  # Old root becomes child of new root
            s.split_child(0)  # Split the old root
            self.root = s  # Update the root
            s.insert_non_full(key)  # Insert the key into the new root
        else:
            root.insert_non_full(key)

    def traverse(self):
        if self.root:
            self.root.traverse()

    def search(self, key):
        if self.root:
            return self.root.search(key)
        return False


# Example usage
if __name__ == "__main__":
    btree = BTree(3)  # Create a B-tree of minimum degree 3
    for key in [10, 20, 5, 6, 12, 30, 7, 17]:
        btree.insert(key)

    print("Traversal of B-tree:")
    btree.traverse()  # Should print keys in sorted order
    print()

    search_key = 6
    print(f"Search {search_key}: {'Found' if btree.search(search_key) else 'Not Found'}")
