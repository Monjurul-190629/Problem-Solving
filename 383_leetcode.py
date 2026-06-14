class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a1 = list(ransomNote);
        a2 = list(magazine)
        if len(a2) < len(a1):
            return False
        else:
            for i in range(len(a1)):
                if a1[i] not in a2:
                    return False
                else:
                    a2.remove(a1[i])
        return True     # O (n*n)



sol = Solution();
print(sol.canConstruct("aab", "aba"))

# /* Better Approach

# from collections import Counter

# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         count = Counter(magazine)

#         for ch in ransomNote:
#             if count[ch] == 0:
#                 return False
#             count[ch] -= 1

#         return True

# */