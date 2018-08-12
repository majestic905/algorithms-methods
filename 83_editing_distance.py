s1 = input()
s2 = input()

if len(s1) > len(s2):
    s1, s2 = s2, s1

prev = list(range(len(s2) + 1))
for i in range(1, len(s1)+1):
    curr = [i]
    for j in range(1, len(s2)+1):
        curr.append(min(curr[-1] + 1, prev[j] + 1, prev[j-1] + (s1[i-1] != s2[j-1])))
    prev = curr

print(prev[-1])
