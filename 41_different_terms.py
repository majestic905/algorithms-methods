n, terms, i = int(input()), [], 1
while n > 2*i:
    terms.append(i)
    n, i = n - i, i + 1
print(len(terms) + 1)
print(*terms, n)