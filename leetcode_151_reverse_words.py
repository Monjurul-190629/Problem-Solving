class Solution:
    def reverseWords(self, s: str) -> str:
        arrStr = s.strip().split()
        arrStr = arrStr[::-1]
        return " ".join(arrStr) 

sol = Solution()
print(sol.reverseWords("  hello world  "));