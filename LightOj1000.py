t = int(input())

for i in range(t):
    np = int(input())
    c1, c2 = 0, 0
    if np > 10:
        c1 = np - 10
        c2 = 10
    else: 
        c1 = 0
        c2 = np
    print(f'{c1} {c2}')