'''

Given a set of intervals, for each of the interval i, check if there exists
an interval j whose start point is bigger than or equal to the end point of the
interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which
means that the interval j has the minimum start point to build the "right"
relationship for interval i. If the interval j doesn't exist, store -1 for the
interval i. Finally, you need output the stored value of each interval as an
array.

'''
from trees.binary_tree import BinarySearchTree


class IntervalNode:
    ''' Added all the special methods to allow
    for use in the binary tree.
    '''
    def __init__(self, left_val, index):
        self.left_val = left_val
        self.index = index

    def __ge__(self, other):
        return self.left_val >= other

    def __le__(self, other):
        return self.left_val <= other

    def __lt__(self, other):
        return self.left_val < other

    def __gt__(self, other):
        return self.left_val > other

    def __sub__(self, other):
        return self.left_val - other

class solution:
    def findRightInterval(self, intervals):
        answers = []
        bst = BinarySearchTree()
        for index, (left, _) in enumerate(intervals):
            node = IntervalNode(left, index)
            bst.add(node)

        for _, right in intervals:
            nearest = bst.find_nearest(right)
            print(nearest)
            if nearest is None:
                answers.append(-1)

            else:
                answers.append(nearest.index)

        return answers


if __name__ == '__main__':
    s = solution()

    print(s.findRightInterval([ [1,4], [2,3], [3,4] ]))
    print(s.findRightInterval([ [3,4], [2,3], [1,2] ]))
