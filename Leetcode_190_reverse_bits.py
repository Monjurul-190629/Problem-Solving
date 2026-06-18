class Solution:
    def reverseBits(self, n: int) -> int:
        # binaryForm = bin(n)[2:]
        # binaryFormWithBits = binaryForm.zfill(32)
        # reverseForm = binaryFormWithBits[::-1]
        # ans = int(reverseForm, 2)
        # return ans
        # time complexity o(k) and space complexity o(1)
        result = 0
        for _ in range(32):
            bit = n & 1
            result = (result << 1) | bit
            n = n >> 1   
        return result   # time complexity O(K) and space complexity O(1)

sol = Solution()
print(sol.reverseBits(6))