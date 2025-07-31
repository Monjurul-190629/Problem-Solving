import math

T = int(input())
pi = 2 * math.acos(0.0)

for case_num in range(1, T + 1):
    r = float(input())
    shaded_area = (4 - pi) * (r ** 2)
    print(f"Case {case_num}: {shaded_area:.2f}")
