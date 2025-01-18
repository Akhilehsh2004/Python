class BPlusTreeNode:
    def __init__(self, t, is_leaf=True):
        self.t = t  # Minimum degree
        self.is_leaf = is_leaf  # True if the node is a leaf
        self.keys = []  # List of keys
        self.children = []  # List of child pointers (if internal node)
        self.next = None  # Pointer to the next leaf node (used only in leaf nodes)


class BPlusTree:
    def __init__(self, t):
        self.t = t  # Minimum degree
        self.root = BPlusTreeNode(t)

    def search(self, key, node=None):
        if node is None:
            node = self.root

        if node.is_leaf:  # If leaf node
            if key in node.keys:
                return True
            return False
        else:  # If internal node
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            return self.search(key, node.children[i])

    def insert(self, key):
        root = self.root
        if len(root.keys) == 2 * self.t - 1:  # If root is full
            new_root = BPlusTreeNode(self.t, is_leaf=False)
            new_root.children.append(self.root)  # Old root becomes child
            self.split_child(new_root, 0)
            self.root = new_root
            self.insert_non_full(new_root, key)
        else:
            self.insert_non_full(root, key)

    def insert_non_full(self, node, key):
        if node.is_leaf:  # Insert into a leaf node
            i = len(node.keys) - 1
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:  # Insert into an internal node
            i = len(node.keys) - 1
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == 2 * self.t - 1:  # If child is full
                self.split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], key)

    def split_child(self, parent, index):
        t = self.t
        full_node = parent.children[index]
        new_node = BPlusTreeNode(t, full_node.is_leaf)

        # Move half the keys to the new node
        new_node.keys = full_node.keys[t:]
        full_node.keys = full_node.keys[:t - 1]

        # Move half the children if it's not a leaf
        if not full_node.is_leaf:
            new_node.children = full_node.children[t:]
            full_node.children = full_node.children[:t]

        # Update the parent
        parent.keys.insert(index, full_node.keys.pop())
        parent.children.insert(index + 1, new_node)

        # If leaf, link new_node to full_node
        if full_node.is_leaf:
            new_node.next = full_node.next
            full_node.next = new_node

    def traverse(self):
        if not self.root:
            return []
        node = self.root
        while not node.is_leaf:  # Go to the leftmost leaf
            node = node.children[0]

        result = []
        while node:
            result.extend(node.keys)
            node = node.next
        return result


# Example Usage
if __name__ == "__main__":
    bpt = BPlusTree(3)  # B+ Tree of minimum degree 3
    keys = [10, 20, 5, 6, 12, 30, 7, 17]

    print("Inserting keys into B+ Tree:")
    for key in keys:
        print(f"Inserting {key}")
        bpt.insert(key)

    print("\nTraversal of B+ Tree (sorted keys):")
    print(bpt.traverse())

    search_key = 12
    print(f"\nSearch {search_key}: {'Found' if bpt.search(search_key) else 'Not Found'}")

    search_key = 25
    print(f"Search {search_key}: {'Found' if bpt.search(search_key) else 'Not Found'}")
