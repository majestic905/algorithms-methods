def merge_sort(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        a = arr[:len(arr) // 2]
        b = arr[len(arr) // 2:]

        a, ai = merge_sort(a)
        b, bi = merge_sort(b)
        c = []

        i, j = 0, 0
        inversions = ai + bi

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            inversions += (len(a) - i)

    c += a[i:]
    c += b[j:]

    return c, inversions

input()
array = list(map(int, input().split()))
print(merge_sort(array)[1])