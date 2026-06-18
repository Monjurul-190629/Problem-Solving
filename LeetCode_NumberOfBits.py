class Solution:
    def hammingWeight(self, n: int) -> int:
        # bn = bin(n)[2:]
        # return str(bn).count("1") # time complextiy o(n) and space complexity o(n)
        count = 0
        while n:
           n &= (n-1)
           count += 1  # time complexity o(1) space complexity o(1)
        return count

sol = Solution()
print(sol.hammingWeight(5))