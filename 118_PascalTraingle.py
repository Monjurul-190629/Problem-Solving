class Solution:
    def generate(self, numRows: int) -> list[list[int]]:

        triangle = []

        for row in range(numRows):

            # Create row filled with 1
            current_row = [1] * (row + 1)

            # Fill middle values
            for col in range(1, row):

                current_row[col] = (
                    triangle[row - 1][col - 1]
                    + triangle[row - 1][col]
                )

            triangle.append(current_row)

        return triangle