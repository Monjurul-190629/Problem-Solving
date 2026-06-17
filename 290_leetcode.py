class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s1 = s.split()
        pattern_to_s1 = {}
        s1_to_pattern = {}

        if len(pattern) != len(s1):
            return False
       
        for c1, c2 in zip(pattern, s1):
            if c1 in pattern_to_s1 and pattern_to_s1[c1] != c2:
               return False
            
            if c2 in s1_to_pattern and s1_to_pattern[c2] != c1:
               return False
        
            pattern_to_s1[c1] = c2
            s1_to_pattern[c2] = c1

        return True
    

sol = Solution()
print(sol.wordPattern("aaa", "aa aa aa aa"))