t = int(input())

for i in range(t):
    p, l = map(int, input().split())
    q = p - l
    result = []
    j = 1
    while j * j <= q:
        if(q % j == 0): 
            d1 = j
            d2 = q // j
            if(d1 > l):
                result.append(d1)
            if(d1 != d2 and d2 > l):
                result.append(d2)
        j += 1
    result.sort()
    if(len(result)> 0): 
        print(f'Case {i+1}:',*result)
    else:
        print(f'Case {i+1}: impossible')
    