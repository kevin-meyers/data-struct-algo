from utils.key_defaultdict import KeyDefaultDict
from histogram import Histogram
from trees.word_freq_tree import WordFreqTree


START_TAG = '#START'
END_TAG = '#END'


class MarkovNode:
    def __init__(self, word):
        self.word = word
        self.transitions_hist = Histogram()
        self.transitions_tree = None

    def add_word(self, word, next_node):
        self.transitions_hist.add_word(word, next_node)

    def hists_to_tree(self):
        self.transitions_tree = WordFreqTree(self.transitions_hist)

    def __str__(self):
        return self.word


class MarkovChain:
    def __init__(self):
        self.start = None
        self._word_pointers = KeyDefaultDict(lambda x: self._new_word(x))
        self.num_types = 0
        self.num_tokens = 0

    def _new_word(self, key):
        self.num_types += 1

        return MarkovNode(key)

    @staticmethod
    def read_file(file_path):
        f = open(file_path, 'r')
        for line in f:
            for word in line.split():
                yield word

            yield END_TAG # each line has an end, will be more sophisticated


    def add_text_to_hists(self, file_path):
        last_word = START_TAG
        for word in self.read_file(file_path):
            self._word_pointers[last_word].add_word(
                word, self._word_pointers[word]
            )
            last_word = word


    def complete_chain(self):
        for _, node in self._word_pointers.items():
            node.hists_to_tree()

        self.start = self._word_pointers[START_TAG]
        self._word_pointers = None



if __name__ == '__main__':
    mc = MarkovChain()
    mc.add_text_to_hists('data/test.txt')
    mc.complete_chain()
    
    word_node = mc.start.transitions_tree.sample()
    words = 0

    while word_node.word is not END_TAG:
        print(word_node.word)
        words += 1
        word_node = word_node.transitions_tree.sample()
