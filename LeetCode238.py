class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ansArr = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if j != i:
                    product *= nums[j]
            ansArr.append(product)
        return ansArr

sol = Solution()
print(sol.productExceptSelf([2, 2, 2]))