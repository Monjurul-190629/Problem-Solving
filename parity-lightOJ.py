t = int(input())
for i in range(t):
   n = int(input())
   b = bin(n)
   ans = b.count("1")
   if ans % 2 == 0: print(f'Case {i+1}: even')
   else: print(f'Case {i+1}: odd')