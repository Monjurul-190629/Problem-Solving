class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        # for i in range(k):
        #     nums.insert(0, nums.pop())
        # for optimal
        k %= len(nums)
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1    
        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)
        return nums

sol = Solution()
print(sol.rotate([1, 2, 3, 4, 5, 6, 7], 3))  # time complexity O(n) space complexity O(