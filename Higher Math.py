t = int(input())
result = []
for _ in range(t):
    sides = list(map(int, input().split()))
    max_side = max(sides)
    sum_of_two_sides = 0
    for i in range(len(sides)):
        if(max_side != sides[i]):
            sum_of_two_sides += sides[i]*sides[i]
    if(max_side*max_side == sum_of_two_sides):
        result.append("yes")
    else:
        result.append("no")

for i in range(t):
    print(f'Case {i + 1}: {result[i]}')