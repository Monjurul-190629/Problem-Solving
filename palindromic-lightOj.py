t = int(input())

for i in range(t):
    n = int(input())
    li = []
    while n != 0:
        rem = n % 10
        li.append(rem)
        n = n // 10
    li1 = li[:]
    li.reverse()
    if(li == li1): print(f'Case {i + 1}: Yes')
    else: print(f'Case {i + 1}: No')
    