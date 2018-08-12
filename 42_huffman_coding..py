from itertools import groupby
from heapq import *


class Node:
    def __init__(self, i, w):
        self.left = None
        self.right = None
        self.item = i
        self.weight = w

    def __repr__(self):
        return "%s - %s — %s _ %s" % (self.item, self.weight, self.left, self.right)

    def __lt__(self, a):
        return self.weight < a.weight


def huffman(string):
    def get_codes(code, node):
        if node.item:
            codes[node.item] = code or '0'
        else:
            get_codes(code + '0', node.left)
            get_codes(code + '1', node.right)

    itemqueue = [Node(a, len(list(b))) for a, b in groupby(sorted(string))]
    heapify(itemqueue)
    while len(itemqueue) > 1:
        right = heappop(itemqueue)
        left = heappop(itemqueue)
        node = Node(None, left.weight + right.weight)
        node.left = left
        node.right = right
        heappush(itemqueue, node)

    codes = {}
    get_codes('', itemqueue[0])
    return codes, ''.join([codes[a] for a in string])


codes, encoded = huffman(input())
print(len(codes), len(encoded))
for item in codes.items():
    print('%s: %s' % item)
print(encoded)
