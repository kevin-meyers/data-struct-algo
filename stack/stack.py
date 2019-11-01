

class Node:
    def __init__(self, data):
        self.under = None
        self.data = data


class Stack:
    def __init__(self):
        self.top = None
        self.height = 0

    def push(self, data):
        node = Node(data)
        if not self.top:
            self.top = node

        else:
            node.under = self.top
            self.top = node

        self.height += 1

    def pop(self):
        if not self.top:
            return None

        data = self.top.data
        self.top = self.top.under
        self.height -= 1

        return data

    def peek(self):
        return self.top.data if self.top else None
