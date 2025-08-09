import math

t = int(input())
for k in range(t):
    r = float(input())
    square = math.pow(2 * r,2)
    circle = math.pi * math.pow(r, 2)
    ans = square - circle
    print(f"Case {k + 1}: {ans:.2f}")