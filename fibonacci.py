n = int(input("Enter which number: "))

fibo_arr = [0, 1]

for i in range(2, n+1):
    fibo_arr.append(fibo_arr[i-1] + fibo_arr[i-2])

print(f"fibonacci number of {n} : ", fibo_arr[n])

