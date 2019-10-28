from unidecode import unidecode
import sys
import cProfile

class Node:
    def __init__(self, letter):
        self.pointers = [False]*27
        self.value = letter


class Tree:
    def __init__(self):
        self.root = Node(['#START'])

    def add_word(self, word, node=None):
        if not node:
            node = self.root

        if len(word) == 1:
            node.pointers[26] = '#END'
            return

        head, tail = ord(word[0]) - 97, word[1:]

        next_node = node.pointers[head]
        if not next_node:
            next_node = Node(word[0])
            node.pointers[head] = next_node

        self.add_word(tail, next_node)


    def find_words(self, node=None):
        if not node:
            print('this will return all words...')
            return ValueError

        if node == '#END':
            return ['']

        return [
            node.value + value
            for pointer in node.pointers if
            pointer for value in self.find_words(pointer)
        ]

    def complete_words(self, starting_letters):
        current_node = self.root

        for letter in starting_letters:
            current_node = current_node.pointers[ord(letter) - 97]

        return [starting_letters[:-1] + ending for ending in self.find_words(current_node)]

    def build_tree(self):
        with open('/usr/share/dict/american-english', 'r') as f:
            for word in f:
                if not word.strip().isalpha():
                    continue

                self.add_word(list(unidecode(word.strip().lower())) + ['#END'])




if __name__ == '__main__':
    t = Tree()
    t.build_tree()
    print(t.complete_words(sys.argv[1]))

