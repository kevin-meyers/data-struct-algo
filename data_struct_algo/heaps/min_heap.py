
class MinHeap:
    def __init__(self):
        self._heap_list = [0]  # Convention to reduce -1s
        self.length = 0

    def __len__(self):
        return self.length

    def pop(self):
        ''' Remove the root node and set root = most_recent. '''
        self._swap(1, self.length)
        item = self._heap_list.pop()
        self.length -= 1
        self._sink(1)
        return item

    def _minindex(self, index):
        if index * 2 + 1 > len(self):  # If it goes outside the list
            return index * 2

        elif self._compare(lambda x, y: x < y, index*2, index*2+1):
            return index * 2

        else:
            return index * 2 + 1

    def _sink(self, index):
        ''' After the root has been replaced with most_recent, sink it down to
        its proper place.

        '''
        while index*2 <= len(self):
            mi = self._minindex(index)
            if self._compare(lambda x, y: x > y, index, mi):
                self._swap(index, mi)

            index = mi

    def push(self, data):
        ''' Add node to the end of the tree, '''
        self.length += 1
        self._heap_list.append(data)
        self._arrange(len(self))

    def _swap(self, index_1, index_2):
        self._heap_list[index_1], self._heap_list[index_2] = \
        self._heap_list[index_2], self._heap_list[index_1]

    def _compare(self, func, index_1, index_2):
        return func(self._heap_list[index_1], self._heap_list[index_2])

    def _arrange(self, index):
        # while (parent_index := k//2) > 0:
        while index // 2 > 0:  # Compare between parent and child
            if self._compare(lambda x, y: x < y, index, index//2):
                self._swap(index, index//2)

            index //= 2 # "moving" up the tree


if __name__ == '__main__':
    h = MinHeap()
    for i in [4, 8, 7, 2, 9, 10, 5, 1, 3, 6]:
        h.push(i)
    
    print(h._heap_list)
    while len(h) > 0:
        print(h.pop())
        print(h._heap_list)
