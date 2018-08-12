n = int(input())
A = list(map(int, input().split()))

D = [0]*n
for i in range(n):
    D[i] = 1
    for j in range(i):
        if A[i] % A[j] == 0 and D[j] + 1 > D[i]:
            D[i] = D[j] + 1

print(max(D))
