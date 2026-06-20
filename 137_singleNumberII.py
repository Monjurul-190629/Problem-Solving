# from collections import Counter
# class Solution:
#     def singleNumber(self, nums: list[int]) -> int:
#         for i in range(len(nums)):
#             if nums.count(nums[i]) == 1:
#                 return nums[i]
# time complexity o(n) space complexity o(n)


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0

        for i in range(32):
            bit_sum = 0

            for num in nums:
                if num & (1 << i):
                    bit_sum += 1

            if bit_sum % 3:
                result |= (1 << i)

        return result

sol = Solution()
print(sol.singleNumber([2, 2, 3, 2]))