input()
counts = [0] * 11
for num in list(map(int, input().split())):
    counts[num] += 1
for i in range(11):
    for j in range(counts[i]):
        print(i, end=' ')