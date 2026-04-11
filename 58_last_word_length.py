# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         arr = s.strip().split()
#         return len(arr[len(arr) - 1])
        
        
# sol = Solution()
# print(sol.lengthOfLastWord("   fly me   to   the moon  "))   time complexity: O(n) space complexity: O(n)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1
        
        # Skip trailing spaces
        while i >= 0 and s[i] == " ":
            i -= 1
        
        # Count last word
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        
        return length   # time comp O(n) space complexity O(1)