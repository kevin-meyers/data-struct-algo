import os
import sys
from data_struct_algo.stack.stack import Stack


class StackQueue:
    def __init__(self):
        self.inbound = Stack()
        self.outbound = Stack()
        self.length = 0

    def __len__(self):
        return self.length

    def __iter__(self):
        for _ in range(len(self)):
            yield self.dequeue()

    def enqueue(self, data):
        if len(self.outbound) != 0:
            self.inbound.push_many(self.outbound)

        self.length += 1
        self.inbound.push(data)

    def dequeue(self):
        if len(self.inbound) != 0:
            self.outbound.push_many(self.inbound)

        self.length -= 1

        return self.outbound.pop()


if __name__ == '__main__':
    sq = StackQueue()

    for i in range(10):
        sq.enqueue(i)

    for i in range(10):
        print(sq.dequeue())
