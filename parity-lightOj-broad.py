t = int(input())
for i in range(t):
    n = int(input())
    li = []
    while n != 0:
        rem = n % 2
        li.append(rem)
        n = n // 2
    li.reverse()
    ans = ''.join(str(x) for x in li)
    print(ans)