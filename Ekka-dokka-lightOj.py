t = int(input())

def check(n):
    return n % 2

for i in range(t):
    w = int(input())
    if(w % 2 == 1):
        print(f'Case {i+1}: Impossible' )
    else:
        # for m in range(2, w, 2):
        #     for n in range(1, w-1, 2):
        #         if(n * m == w):
        #             print(f"Case {i+1}: {n} {m}")
        #             break
        # it gets time limit exceeded
        n = w
        while n % 2 == 0:
            n = n // 2
        m = w // n
        print(f"Case {i+1}: {n} {m}")
    