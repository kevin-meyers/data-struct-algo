

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def __iter__(self):
        current = self.head
        for _ in range(len(self)):
            yield current.data
            current = current.next

    def append(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            self.tail= node

    def __contains__(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True

            current = current.next

        return False

    def delete(self, data):
        current = self.head
        previous = None
        while current:
            if current.data == data:
                break

            previous = current
            current = current.next

        if current == None:
            raise ValueError('data not in list')

        if previous == None:
            self.head = self.head.next

        else:
            previous.next = current
