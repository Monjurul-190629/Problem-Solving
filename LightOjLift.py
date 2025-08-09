t = int(input())
for i in range(t):
    y, l = map(int, input().split())
    diff = 0
    # we can use abs(y-l)
    if(y > l):
        diff = y - l
    else:
        diff = l - y
    ans = (y * 4) + (diff * 4) + 9 + 10
    print(f'Case {i + 1}: {ans}')