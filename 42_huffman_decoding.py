k, _ = map(int, input().split())
lut = dict([reversed(input().split(': ')) for _ in range(k)])
encoded = input()
while len(encoded) > 0:
    for code in lut:
        if encoded.startswith(code):
            print(lut[code], end='')
            encoded = encoded[len(code):]