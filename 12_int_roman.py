# class Solution:
#     def intToRoman(self, num: int) -> str:
#         ansStr = ''
#         while num != 0:
#             if num >= 1000:
#                 res = num // 1000;
#                 ansStr += "M" * res;
#                 num -= res * 1000;
#             elif num >= 500:
#                 if num >= 900:
#                     ansStr += "CM"
#                     num -= 900
#                 else:
#                     ansStr += "D"
#                     num -= 500
#             elif num >= 100:
#                 if num>=400:
#                     ansStr += "CD"
#                     num -= 400
#                 else:
#                     ansStr += "C" * (num // 100)
#                     num -= 100 * (num // 100)
#             elif num >= 50:
#                 if num >= 90:
#                    ansStr+= "XC"
#                    num -= 90
#                 else:
#                     ansStr += "L" 
#                     num -= 50
#             elif num >= 10:
#                 if num >= 40:
#                    ansStr += "XL"
#                    num -= 40
#                 else:
#                    ansStr += "X" * (num // 10)
#                    num -= 10 * (num // 10)
#             elif num >= 5:
#                 if num == 9:
#                    ansStr += "IX"
#                    num -= 9
#                 else:
#                    ansStr += "V"
#                    num -= 5
#             else:
#                 if num == 4:
#                    ansStr += "IV"
#                    num -= 4
#                 else:
#                    ansStr += "I" * num
#                    num -= num
#         return ansStr
        
        
        
        
# sol = Solution()
# print(sol.intToRoman(58))


class Solution:
    def intToRoman(self, num: int) -> str:
        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        
        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]
        
        result = ""
        
        for i in range(len(values)):
            while num >= values[i]:
                result += symbols[i]
                num -= values[i]
        
        return result
        
sol = Solution()
print(sol.intToRoman(39))