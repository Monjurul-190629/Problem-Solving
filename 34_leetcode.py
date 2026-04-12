class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        
        def findFirst():
            start, end = 0, len(nums) - 1
            first = -1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    first = mid
                    end = mid - 1   # go left
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return first
        
        def findLast():
            start, end = 0, len(nums) - 1
            last = -1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    last = mid
                    start = mid + 1   # go right
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return last
        
        return [findFirst(), findLast()]