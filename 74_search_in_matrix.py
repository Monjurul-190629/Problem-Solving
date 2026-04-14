class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # brute force
        # matrixlen = len(matrix)
        # for i in range(matrixlen):
        #     if target in matrix[i]:
        #         return True
        # return False
        # optimal solution
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        start = 0
        end = m * n - 1
        while start <= end:
            mid = (start + end) // 2
            row = mid // n
            col = mid % n
            value = matrix[row][col]
            if value == target:
                return True
            elif value < target:
                start = mid + 1
            elif value > target:
               end = mid - 1
        return False


sol = Solution()
print(sol.searchMatrix([[1]], 1))