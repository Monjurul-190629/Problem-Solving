class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        result = 0
        for i in range(left+1, right + 2):
            result = result & left
        return result

sol = Solution()
print(sol.rangeBitwiseAnd(5, 7))