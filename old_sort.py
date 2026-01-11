t = int(input())

for k in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    swap = 0
    for i in range(n):
        while arr[i] != i + 1:
            correct_index = arr[i] - 1
            arr[i], arr[correct_index] = arr[correct_index], arr[i]
            swap += 1
    print(f'Case {k + 1}: {swap}')