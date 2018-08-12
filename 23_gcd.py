a, b = map(int, input().split())
while b:
    a, b = b, a % b
print(a)

# from math import gcd
# print(gcd(*map(int, input().split())))