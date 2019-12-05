

class CircularBuffer(list):
    def __init__(self, fixed_size):
        self.max_size = fixed_size
        self.extend([None for _ in range(self.max_size)])
        self.head = 0
        self.length = 0

    def __len__(self):
        return self.length

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

    def enqueue(self, data):
        index = (self.head + len(self)) % self.max_size
        self[index] = data
        self._add()

    def _add(self):
        if len(self) == self.max_size:
            self._move_head()

        else:
            self.length += 1

    def _move_head(self):
        self.head += 1
        if self.head >= self.max_size:
            self.head = 0

    def _remove(self):
        self.length -= 1
        self._move_head()

    def dequeue(self):
        item = self[self.head]
        if item is None:
            raise ValueError('Buffer is empty.')

        self[self.head] = None
        self._remove()

        return item


if __name__ == '__main__':
    cb = CircularBuffer(3)
    for num in range(4):  # 0 should get overwritten
        cb.enqueue(num)

    for num in cb:
        print(num)
