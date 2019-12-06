import random

from collections import deque


class Node:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        self.right = None
        self.left = None


class WordFreqTree:
    def __init__(self, hist=None):
        self.root = None
        self.length = 0
        if hist:
            hist_list = list(hist.get_proba_offset())
            random.shuffle(hist_list)
            self.build_tree(hist_list)

    def add(self, new_node):
        if self.root is None:
            self.root = new_node

        else:
            current = self.root

            while True:
                if new_node.freq < current.freq:
                    if current.left is None:
                        current.left = new_node
                        break

                    else:
                        current = current.left

                else:
                    if current.right is None:
                        current.right = new_node
                        break

                    else:
                        current = current.right

    def __len__(self):
        return self.length


    def _find_word(self, val, node):
        if val < node.freq:
            if node.left is None:
                return node.word

            self._find_word(val, node.left)

        else:
            if node.right is None:
                return node.word

            self._find_word(val, node.right)


    def sample(self):
        rand = random.random()
        if self.root is None:
            raise ValueError('Tree not built yet, try build_tree')

        current = self.root
        while True:
            if rand < current.freq:
                if current.left is None:
                    return current.word

                current = current.left

            else:
                if current.right is None:
                    return current.word

                current = current.right


    def build_tree(self, shuffled_word_freqs):
        for word, freq in shuffled_word_freqs:
            node = Node(word, freq)

            self.add(node)

