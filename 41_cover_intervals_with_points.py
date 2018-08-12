n = int(input())
intervals = [list(map(int, input().split())) for _ in range(n)]
intervals.sort(key=lambda x: x[1])

def intersect(a, b):
    a, b = max(a[0], b[0]), min(a[1], b[1])
    return None if b < a else [a, b]

intersections = []
current = intervals[0]
for interval in intervals[1:]:
    intersection = intersect(current, interval)
    if intersection is None:
        intersections.append(current)
        current = interval
    else:
        current = intersection
intersections.append(current)

print(len(intersections))
print(*list(zip(*intersections))[1])