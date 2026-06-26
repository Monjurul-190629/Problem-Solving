class Solution:
    def canJump(self, nums: list[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] <=  nums[i]:
                pass
            else:
                return False
        return True

sol = Solution()
print(sol.canJump([2,3,1,1,4]))
        