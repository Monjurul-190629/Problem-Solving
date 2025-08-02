import sys
input = sys.stdin.readline

def min_moves(dusts, w):
    dusts.sort(key=lambda x: x[1])  # Sort by y-coordinate
    n = len(dusts)
    i = 0
    moves = 0

    while i < n:
        start_y = dusts[i][1]
        end_y = start_y + w
        moves += 1

        # Skip all dusts that are within this vertical interval
        while i < n and dusts[i][1] <= end_y:
            i += 1

    return moves

T = int(input())
for case_num in range(1, T + 1):
    input()  # blank line
    N, w = map(int, input().split())
    dusts = [tuple(map(int, input().split())) for _ in range(N)]

    result = min_moves(dusts, w)
    print(f"Case {case_num}: {result}")
