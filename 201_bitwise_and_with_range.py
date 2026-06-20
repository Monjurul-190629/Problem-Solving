class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shifts = 0
        while left != right:
            left  >>= 1
            right >>= 1
            shifts += 1
        ans = left << shifts
        return ans

sol = Solution()
print(sol.rangeBitwiseAnd(5, 7))