class Solution:
    def canJump(self, nums: list[int]) -> bool:
        maxReach = 0
        for i in range(len(nums)):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i + nums[i])
        return True

sol = Solution()
print(sol.canJump([2,3,1,1,4]))
        