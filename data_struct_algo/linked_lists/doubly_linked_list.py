

class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def __iter__(self):
        current = self.head
        for _ in range(len(self)):
            yield current
            current = current.next


    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node

        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node

        self.length += 1

    def delete(self, data):  # Make a note if deleted or valueerror if not
        if self.head.data == data:
            self.head = self.head.next

        elif self.tail.data == data:
            self.tail = self.tail.previous

        else:
            for node in self:
                if node.data == data:
                    node.previous.next = node.next
                    node.next.previous = node.previous
