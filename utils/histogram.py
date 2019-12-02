from collections import defaultdict


class HistNode:
    def __init__(self, markov_node):
        self.freq = 1
        self.markov_node = markov_node

    def __repr__(self):
        return str(self.freq) + ' ' + str(self.markov_node)

class Histogram:
    def __init__(self):
        self.unique_words = 0
        self.num_words = 0
        self.hist = {}

    def __len__(self):
        return self.unique_words

    def __str__(self):
        return str(self.hist)

    @staticmethod
    def _open_file(filepath):
        f = open(filepath, 'r')
        for line in f:
            for word in line.split():
                yield word

    def add_word(self, word, markov_node):
        if word in self.hist:
            node = self.hist[word]
            node.freq += 1

        else:
            self.hist[word] = HistNode(markov_node)
            self.unique_words += 1

        self.num_words += 1

#    def build_histogram(self, filepath):  CLOSED DUE TO CONSTRUCTION
#        for word in self._open_file(filepath):
#            self.add_word(word)

    def get_frequency(self, word):
        return self.hist[word].freq

    def get_proba_offset(self):
        running_sum = 0.0
        for node in self.hist.values():
            running_sum += node.freq / self.num_words
            yield node.markov_node, running_sum


if __name__ == '__main__':
    hist = Histogram()
    hist.build_histogram('data/test.txt')

    print(hist.hist)
