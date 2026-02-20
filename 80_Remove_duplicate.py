class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        c = 2
        for i in range(2, len(nums)):
            if(nums[i] != nums[c - 2]):
                nums[c] = nums[i]
                c += 1
        return c, nums
sol = Solution()
print(sol.removeDuplicates([1, 1, 1, 2, 2, 3]))  # time complexity O(n) space complexity O(1)