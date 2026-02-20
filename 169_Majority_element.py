class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # for i in range(len(nums)):
        #     ans = nums.count(nums[i])
        #     if ans > len(nums) / 2:
        #         return nums[i]
        # time limti exceeded
        # time limit exceeded
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(len(nums)):
        #         if(nums[i] == nums[j]):
        #             count += 1
        #     if count > len(nums) / 2:
        #         return nums[i]
        # Boyre Moore voting algorithm
        count = 0
        candidate = None
        for i in nums:
            if count == 0:
                candidate = i
            if i == candidate:
                count += 1
            else:
                count -= 1
        return candidate
            

sol = Solution()
print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # time complexity O(n^2) space complexity O( 1)