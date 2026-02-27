# class Solution:
#     def romanToInt(self, s: str) -> int:
#         num = 0
#         i = 0
#         while i < len(s):
#             if s[i] == "M":
#                 num += 1000
#             elif s[i] == "D":
#                 num += 500
#             elif s[i] == "C":
#                 if i+1 < len(s) and s[i + 1] == "M":
#                     num += 900
#                     i += 1
#                 elif i+1 < len(s) and s[i + 1] == "D":
#                     num += 400
#                     i += 1
#                 else:
#                     num += 100
#             elif s[i] == "L":
#                     num += 50
#             elif s[i] == "X":
#                 if i+1 < len(s) and s[i + 1] == "C":
#                     num += 90
#                     i += 1
#                 elif i+1 < len(s) and s[i + 1] == "L":
#                     num += 40
#                     i += 1
#                 else:
#                     num += 10
#             elif s[i] == "V":
#                 num += 5
#             else:
#                 if i+1 < len(s) and s[i + 1] == "X":
#                     num += 9
#                     i += 1
#                 elif i+1 < len(s) and s[i + 1] == "V":
#                     num += 4
#                     i += 1
#                 else:
#                     num += 1
#             i += 1
#         return num;
        
# sol = Solution()
# print(sol.romanToInt("MCM"))


# same time complextity + space complexity respectively O(n) and O(1)
class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }
        
        total = 0
        
        for i in range(len(s)):
            if i + 1 < len(s) and values[s[i]] < values[s[i+1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        
        return total
    
sol = Solution()
print(sol.romanToInt("MCM"))
