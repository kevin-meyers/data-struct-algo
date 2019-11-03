

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def inorder_traversal(self, new_root):
        current = new_root
        if current is None:
            return

        self.inorder_traversal(current.left)
        print(current.data)
        self.inorder_traversal(current.right)

