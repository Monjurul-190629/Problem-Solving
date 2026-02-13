class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0):
            return False
        list1 = [int(d) for d in str(x)]
        result = list(reversed(list1))
        if(result == list1):
            return True
        else:
            return False

sol = Solution()
print(sol.isPalindrome(121))