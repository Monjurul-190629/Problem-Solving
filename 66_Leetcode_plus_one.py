class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # in here time complexity is O(n) and space complexity is O(n)
        # str1 = "".join(map(str, digits))
        # return list(map(int, str(int(str1) + 1)))
        # opimal solution is here with time complexity O(n) and space complexity O(1)
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1] + digits
                
        
sol = Solution();
print(sol.plusOne([0, 1, 2, 3]))