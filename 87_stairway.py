input()
p, q = 0, 0
for s in input().split():
    p, q = q, max(p, q)+int(s)
print(q)