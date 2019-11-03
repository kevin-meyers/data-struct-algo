from queues.node_queue import NodeQueue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def breadth_first(self):
        queue = NodeQueue()
        queue.enqueue(self.root)

        while len(queue) > 0:
            node = queue.dequeue()
            yield node.data
            if node.left:
                queue.enqueue(node.left)

            if node.right:
                queue.enqueue(node.right)

    def depth_first():
        pass
