def get_pisano_period(m):
    a, b, i = 1, 1, 1
    while a != 0 or b != 1:
        a, b, i = b, (a + b) % m, i + 1
    return i

def get_fibonacci_modulo(n, m):
    a, b, r = 0, 1, n % get_pisano_period(m)
    for _ in range(1, r):
        a, b = b, (a + b) % m
    return r if r < 2 else b

n, m = map(int, input().split())
print(get_fibonacci_modulo(n, m))