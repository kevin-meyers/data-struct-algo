

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class NodeQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def __iter__(self):
        for _ in range(len(self)):
            yield self.dequeue()

    def enqueue(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node

        self.length += 1

    def dequeue(self):
        if len(self) == 0:
            return None

        data = self.head.data

        if len(self) == 1:
            self.head = None
            self.tail = None

        else:
            self.head = self.head.next

        self.length -= 1
        return data
