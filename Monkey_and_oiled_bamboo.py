t = int(input())

for i in range(t):
    n = int(input())
    heights = list(map(int, input().split()))[:n]

    result = heights[0]          # ground → first rung
    prev = heights[0]

    # find maximum jump
    for j in range(1, n):
        diff = heights[j] - heights[j - 1]
        if result < diff:
            result = diff

    curr_k = result

    # simulate jumps
    if heights[0] == curr_k:
        curr_k -= 1

    for j in range(1, n):
        diff = heights[j] - heights[j - 1]
        if diff > curr_k:
            result += 1
            break
        elif diff == curr_k:
            curr_k -= 1

    print(f'Case {i + 1}:', result)
