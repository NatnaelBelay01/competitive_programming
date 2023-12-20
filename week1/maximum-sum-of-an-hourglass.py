class Solution:

    def maxSum(self, grid: List[List[int]]) -> int:
        def helper(mat , col1 ,row1):
            row2 = row1 + 2
            col2 = col1 + 2
            total = 0
            for row in range(row1, row2 + 1):
                for col in range(col1 , col2 + 1):
                    if((row , col) != (row1 + 1, col1) and (row, col) != (row1 + 1, col2)):
                        print(row, col)
                        total += mat[row][col]
            return total
        result = 0
        for row in range(len(grid) - 2):
            for col in  range(len(grid[0]) - 2):
                result = max(helper(grid, col, row), result)
        return result
        