class Solution:
    def reverseVowels(self, s: str) -> str:
        arrStr = list(s)
        store = []
        vowel = "aeiou"
        for i in range(len(arrStr)):
            if arrStr[i].lower() in vowel:
                store.append(arrStr[i])
        store.reverse()
        n = 0
        for i in range(len(arrStr)):
            if arrStr[i].lower() in vowel:
                arrStr[i] = store[n]
                n += 1
        ans = "".join(arrStr)
        return ans
    
sol = Solution()
print(sol.reverseVowels("leetcode"))