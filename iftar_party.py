t = int(input())

for i in range(t):
    p, l = map(int, input().split())
    q = p - l
    result = []
    for j in range(l+1, q//2 + 1 ):
        if(q % j == 0): result.append(j)
    if(q > l): result.append(q)
    if(len(result)> 0): 
        print(f'Case {i+1}:',*result)
    else:
        print(f'Case {i+1}: impossible')
    