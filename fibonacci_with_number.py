n = int(input("Enter which numbers fibonacci you want: "))

fibo = [0, 1]

for i in range(2, n+1):
    next_fibo = fibo[i-1] + fibo[i-2]
    fibo.append(next_fibo)

print(f"The first {n} Fibonacci numbers are: {fibo[:n]}")