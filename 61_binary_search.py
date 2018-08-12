from bisect import bisect
_, *array = map(int, input().split())
_, *queries = map(int, input().split())
for query in queries:
    pos = bisect(array, query)
    print(pos if array[max(pos-1, 0)] == query else -1, end=' ')