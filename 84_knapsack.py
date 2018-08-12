W, n = map(int, input().split())
w = list(map(int, input().split()))

prev = [0] * (W+1)
for i in range(1, n+1):
    curr = [0] * (W+1)
    for j in range(1, W+1):
        curr[j] = prev[j]
        if w[i-1] <= j:
            curr[j] = max(curr[j], prev[j-w[i-1]] + w[i-1])
    prev = curr

print(prev[-1])