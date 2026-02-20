class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        count = 0
        
        for i in range(len(nums)):
            if(nums[i] != val):
                nums[count] = nums[i]
                count += 1
                
        return count


sol = Solution()
print(sol.removeElement([3, 2, 2, 3], 3))