class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        result = 0

        for row in range(n):
            for col in range(n):
                if(row + col == n-1 or row - col == 0):
                    result += mat[row][col]
        return result