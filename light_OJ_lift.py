t = int(input())
for i in range(t):
    m, l = map(int, input().split())
    n = abs(m-l)
    print(f'Case {i + 1}: ', (n + m)*4 + 9 + 10)