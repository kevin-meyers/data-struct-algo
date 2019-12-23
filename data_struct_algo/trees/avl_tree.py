

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
        node = Node(data)
        if self.root is None:
            self.root = node

        else:
            self._add(current=self.root, new=node)

    def _node_height(self, node):
        if node is None:
            return 0

        return node.height

    def get_balance_factor(self, current):
        if current is None:
            return 0

        return self._node_height(current.right) - self._node_height(current.left)

    def _add(self, current, new):
        if current is None:
            return new

        elif new.data < current.data:
            current.left = self._add(current.left, new)

        else:
            current.right = self._add(current.right, new)

        self.set_height(current)

        balance_factor = self.get_balance_factor(current)


        # Left is imbalanced
        if balance_factor <= -2:
            # Left Left imbalance
            if self.get_balance_factor(current.left) <= -1:
                print('left left')
                return self.right_rotation(current)

            # Left Right imbalance
            else:
                print('left right')
                current.left = self.left_rotation(current.left)
                return self.right_rotation(current)

        # Right is imbalanced
        elif balance_factor >= 2:
            if self.get_balance_factor(current.right) >= 1:
                print('right right')
                return self.left_rotation(current)

            else:
                print('right left')
                current.right = self.right_rotation(current.right)
                return self.left_rotation(current)

        return current

    def set_height(self, current):
         current.height = 1 + max(self._node_height(current.left),
                                 self._node_height(current.right))

    def right_rotation(self, a):
        b = a.left
        c = b.right

        a.left = None
        b.right = a

        self.set_height(a)
        self.set_height(b)

        return b

    def left_rotation(self, a):
        b = a.right
        c = b.left

        a.right = None
        b.left = a

        self.set_height(a)
        self.set_height(b)

        return b

    def preOrder(self, root): 
  
        if not root: 
            return
  
        print("{0} ".format(root.data), end="") 
        self.preOrder(root.left) 
        self.preOrder(root.right) 

if __name__ == '__main__':
    myTree = AVLTree() 
    for num in range(3):
        root = myTree.add(num)

    myTree.preOrder(myTree.root) 
    print() 
