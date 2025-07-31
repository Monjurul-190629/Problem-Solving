T = int(input())
for case_num in range(1, T + 1):
    x1, y1, x2, y2 = map(int, input().split())
    M = int(input())
    print(f"Case {case_num}:")
    for _ in range(M):
        x, y = map(int, input().split())
        if x1 < x < x2 and y1 < y < y2:
            print("Yes")
        else:
            print("No")
