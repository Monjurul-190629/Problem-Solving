def is_possible(vessels, m, max_capacity):
    count = 1
    current_sum = 0

    for milk in vessels:
        if milk > max_capacity:
            return False
        if current_sum + milk > max_capacity:
            count += 1
            current_sum = milk
        else:
            current_sum += milk

    return count <= m


def min_max_container_capacity(vessels, m):
    low = max(vessels)
    high = sum(vessels)
    answer = high

    while low <= high:
        mid = (low + high) // 2
        if is_possible(vessels, m, mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer


# Main input handling
T = int(input())
for case_num in range(1, T + 1):
    n, m = map(int, input().split())
    vessels = list(map(int, input().split()))
    result = min_max_container_capacity(vessels, m)
    print(f"Case {case_num}: {result}")
