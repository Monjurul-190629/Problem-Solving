# class Solution:
#     def mySqrt(self, x: int) -> int:
#         i = 0
#         while i * i <= x:
#             i += 1
#         return i - 1

# sol = Solution()
# print(sol.mySqrt(8))  # time complexity O(root(x))

# optimal solution
class Solution:
    def mySqrt(self, x: int) -> int:
        if(x < 2):
            return x
        left = 1
        right = x // 2
        while left <= right:
            mid = (left + right) // 2
            if(mid * mid == x):
                return mid
            elif mid * mid < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

sol = Solution()
print(sol.mySqrt(8))  # time complexity O(log(x))