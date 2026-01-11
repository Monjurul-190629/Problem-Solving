def lower_bound(arr, x):
    """First index where arr[index] >= x"""
    l, r = 0, len(arr)
    while l < r:
        m = (l + r) // 2
        if arr[m] < x:
            l = m + 1
        else:
            r = m
    return l

def upper_bound(arr, x):
    """First index where arr[index] > x"""
    l, r = 0, len(arr)
    while l < r:
        m = (l + r) // 2
        if arr[m] <= x:
            l = m + 1
        else:
            r = m
    return l

t = int(input())
for case in range(1, t + 1):
    n, q = map(int, input().split())
    points = list(map(int, input().split()))

    print(f"Case {case}:")
    for _ in range(q):
        A, B = map(int, input().split())
        left = lower_bound(points, A)
        right = upper_bound(points, B)
        print(right - left)
