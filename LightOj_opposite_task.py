T = int(input())
for case in range(1, T + 1):
    n = int(input())
    a = min(n, 10)
    b = n - a
    print(f"{b} {a}")
