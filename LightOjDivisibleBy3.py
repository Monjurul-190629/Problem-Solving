T = int(input())
for case_num in range(1, T + 1):
    A, B = map(int, input().split())
    count = 0
    for n in range(A, B + 1):
        digit_sum = n * (n + 1) // 2
        if digit_sum % 3 == 0:
            count += 1
    print(f"Case {case_num}: {count}")
