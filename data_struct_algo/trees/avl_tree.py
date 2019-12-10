

class Node:
    ''' Like a normal treenode except it has height. '''
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None
        self.num_items = 0

    def __len__(self):
        return self.num_items

    def add(self, data):
        node = data
        if self.root is None:
            self.root = node

        else:
            self._add(current=self.root, new=node)

    def _node_height(self, node):
        if node is None:
            return 0

        return node.height

    def _add(self, current, new):
        if new.data < current.data:
            self._add(current.left, new)

        else:
            self._add(current.right, new)




