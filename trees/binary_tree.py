

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.length = 0

    def add(self, data):
        node = TreeNode(data)
        if self.root is None:
            self.root = node

        else:
            self._add(node)

    def _add(self, node):
        current = self.root
        while current:
            if node.data < current.data:
                if current.left is None:
                    current.left = node
                    break

                else:
                    current = current.left

            else:
                if current.right is None:
                    current.right = node
                    break

                else:
                    current = current.right

    def find_nearest(self, data):
        current = self.root
        current_best_node = None
        current_best_distance = None
        while current:
            diff = abs(current.data - data)
            if (
                current_best_distance is None or diff < current_best_distance
            ) and current.data >= data:

                current_best_node = current
                current_best_distance = diff

            if data >= current.data:
                current = current.right

            else:
                current = current.left

        if current_best_node:
            return current_best_node.data
