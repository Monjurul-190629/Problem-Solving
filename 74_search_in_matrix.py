class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        matrixlen = len(matrix)
        for i in range(matrixlen):
            if target in matrix[i]:
                return True
        return False


sol = Solution()
print(sol.searchMatrix([[1]], 1))