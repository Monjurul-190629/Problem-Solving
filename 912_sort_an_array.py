class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums
        pivot = len(nums) // 2
        left = []
        right = []
        middle = []
        for i in range(len(nums)):
            if nums[i] < nums[pivot]:
                left.append(nums[i])
            elif nums[i] > nums[pivot]:
                right.append(nums[i])
            else:
                middle.append(nums[i])
        return self.sortArray(left) + middle + self.sortArray(right)

sol = Solution()
print(sol.sortArray([5, 2, 3, 1]))