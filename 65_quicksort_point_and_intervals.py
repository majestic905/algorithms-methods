from bisect import bisect_left, bisect_right

n, m = map(int, input().split())
A, B = [0]*n, [0]*n
for i in range(n):
    A[i], B[i] = map(int, input().split())
X = list(map(int, input().split()))

A.sort()
B.sort()
for x in X:
    p = bisect_right(A, x)
    q = bisect_left(B, x)
    print(abs(q-p))