n = int(input())
dp, p = [0]*(n+1), [-1]*(n+1)
for i in range(2, n+1):
    res, p[i] = dp[i-1], i-1
    if i % 2 == 0 and dp[i // 2] < res:
        res, p[i] = dp[i // 2], i // 2
    if i % 3 == 0 and dp[i // 3] < res:
        res, p[i] = dp[i // 3], i // 3
    dp[i] = res + 1

print(dp[n])
s, c = [n], n
while p[c] != -1:
    s.append(p[c])
    c = p[c]
print(' '.join(map(str, reversed(s))))