from unidecode import unidecode

START = '#START'
END = '#END'
ASCII_OFFSET = ord('a')  # 97


class Node:
    def __init__(self, letter):
        self.pointers = [False]*27
        self.value = letter


class Tree:
    def __init__(self):
        self.root = Node([START])

    def add_word(self, word, node=None):
        if not node:
            node = self.root

        if len(word) == 1:
            node.pointers[26] = END
            return

        head, tail = ord(word[0]) - ASCII_OFFSET, word[1:]

        next_node = node.pointers[head]
        if not next_node:
            next_node = Node(word[0])
            node.pointers[head] = next_node

        self.add_word(tail, next_node)


    def find_words(self, node=None):
        if not node:
            raise ValueError('this will return all words...')

        if node == END:
            return ['']

        return [
            node.value + value
            for pointer in node.pointers if
            pointer for value in self.find_words(pointer)
        ]

    def complete_word(self, starting_letters):
        current_node = self.root
        try:
            for letter in starting_letters:
                current_node = current_node.pointers[ord(letter) - ASCII_OFFSET]

            if not current_node:  # Without this the previous statement could
                raise             # return False and cause a break later.

        except:
            return 'Those letters dont lead to a word in the dictionary.'

        print(current_node)

        return [starting_letters[:-1] + ending for ending in self.find_words(current_node)]

    def build_tree(self):
        with open('/usr/share/dict/american-english', 'r') as f:
            for word in f:
                if not word.strip().isalpha():
                    continue

                self.add_word(list(unidecode(word.strip().lower())) + [END])




if __name__ == '__main__':
    t = Tree()
    t.build_tree()
    while True:
        user_in = input('enter some letters you want autocompleted type / to quit: ')
        if user_in == '/':
            break

        print(t.complete_word(user_in))

