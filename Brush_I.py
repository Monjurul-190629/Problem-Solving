def main():
    t = int(input().strip())
    result = [];
    for _ in range(t):
        input()
        n = int(input())
        dusts = list(map(int, input().split()))[:n]
        s = 0
        for i in range(len(dusts)):
            if(dusts[i] > 0):
                s += dusts[i]
        result.append(s)
    for i in range(t):
        print(f'Case {i + 1}: {result[i]}')

main()