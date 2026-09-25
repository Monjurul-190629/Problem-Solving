class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [1] * n
        left = 1 
        for i in range(n):
            ans[i] = left
            left = left * nums[i]
        right = 1
        for j in range(n-1, -1, -1):
            ans[j] *= right
            right *= nums[j]
        return ans

sol = Solution()
print(sol.productExceptSelf([2, 2, 2]))