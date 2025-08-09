t = int(input())
for k in range(t):
    n, p, q = map(int, input().split())
    eggs = list(map(int, input().split()))[:n]
    no_of_egg = 0
    sum_of_gm = 0
    for i in range(n):
        sum_of_gm += eggs[i]
        no_of_egg += 1
        if(sum_of_gm > q):
            no_of_egg -= 1
            break
        if(no_of_egg > p):
            no_of_egg -= 1
            break
    print(f'Case {k + 1}: {no_of_egg}')
