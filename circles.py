import math 

T = int(input().strip())

for case in range(1, T + 1):
    R, n = input().split()
    R = float(R)
    n = int(n)

    # Special case: n = 2
    # Two circles touch each other and the big circle
    if n == 2:
        r = R / 2
    else:
       angle = math.pi / n

        # Binary search range
    low, high = 0.0, R

    for _ in range(100):  # sufficient for 1e-6 accuracy
        mid = (low + high) / 2

        # Distance between adjacent centers
        chord = 2 * (R - mid) * math.sin(angle)

        if chord > 2 * mid:
            low = mid
        else:
            high = mid

        r = (low + high) / 2

    print(f"Case {case}: {r:.10f}")