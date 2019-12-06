class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def __iter__(self):
        while len(self) > 0:
            yield self.popleft()

    def __reversed__(self):
        while len(self) > 0:
            yield self.pop()

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node

        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node

        self.length += 1

    def appendleft(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node

        else:
            node.next = self.head
            self.head.previous = node
            self.head = node

        self.length += 1

    def pop(self):
        item = self.tail.data
        if item is None:
            raise ValueError('Queue is empty.')

        self.tail = self.tail.previous
        if self.tail is None:
            self.head = None

        self.length -= 1

        return item

    def popleft(self):
        item = self.head.data
        if item is None:
            raise ValueError('Queue is empty.')

        self.head = self.head.next
        if self.head is None:
            self.tail = None

        self.length -= 1

        return item


if __name__ == '__main__':
    d = Deque()
    for num in range(5,10):
        d.append(num)

    for num in range(4, 0, -1):  # Adding 4321 to the queue on the left
        d.appendleft(num)

    for num in reversed(d):
        print(num)
