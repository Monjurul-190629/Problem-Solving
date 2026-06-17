class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = {}
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i
        return False
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if abs(i - j) <= k and nums[i] == nums[j] and i != j:
        #             return True
        # return False
sol = Solution()
print(sol.containsNearbyDuplicate([1, 0, 1, 1], 1))
print(sol.containsNearbyDuplicate([1,2,3,1], 3))
print(sol.containsNearbyDuplicate([1,2,3,1,2,3], 2))