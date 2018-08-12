from collections import Counter
from heapq import *

def huffman(string):
    def get_codes(code, node):
        if node[2]:
            codes[node[2]] = code or '0'
        else:
            get_codes(code + '0', node[3])
            get_codes(code + '1', node[4])

    itemqueue = [(w, n, i, None, None) for n, (i, w) in enumerate(Counter(string).items())]
    heapify(itemqueue)

    for n in range(len(itemqueue)+1, 2*len(itemqueue)):
        right, left = heappop(itemqueue), heappop(itemqueue)
        node = (left[0] + right[0], n, None, left, right)
        heappush(itemqueue, node)

    codes = {}
    get_codes('', itemqueue[0])
    return codes, ''.join([codes[a] for a in string])

codes, encoded = huffman(input())
print(len(codes), len(encoded))
print(*['%s: %s' % item for item in codes.items()], encoded, sep='\n')