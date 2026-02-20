# using set
# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         count = set(nums)
#         print(count)
#         print(len(count))


# accepted but not optimal
# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         c = 0
#         newArr = []
#         for i in range(len(nums)):
#             if nums[i] not in newArr:
#                 newArr.append(nums[i])
#                 nums[c] = nums[i]
#                 c += 1
#         return c
# sol = Solution()
# print(sol.removeDuplicates([1, 1, 2]))


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        c = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[c -1]:
                nums[c] = nums[i]
                c += 1
        return c
sol = Solution()
print(sol.removeDuplicates([1, 1, 2]))  # time complexity O(n) space complexity O(1)