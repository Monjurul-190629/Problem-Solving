t = int(input())

for i in range(t):
    n, q = map(int, input().split())
    points = list(map(int, input().split()))[:n]
    print(f'Case {i+1}:')
    for _ in range(q):
        s1, s2 = map(int, input().split())
        count = 0
        for j in range(len(points)):
            if s1 <= points[j] <= s2:
                count += 1
        print(count)
        