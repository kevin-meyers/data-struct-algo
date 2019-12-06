

class ListQueue:
    def __init__(self):
        self.items = []
        self.length = 0

    def __len__(self):
        return self.length

    def __iter__(self):
        for _ in range(self.__len__()):
            yield self.dequeue()

    def enqueue(self, data):
        self.items.insert(0, data)
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None

        self.length -= 1
        return self.items.pop()

