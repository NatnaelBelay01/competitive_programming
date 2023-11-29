class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        for i in range(1, m):
            j = i - 1
            k = 1
            while(k < len(matrix[i])):
                if (matrix[j][k-1] != matrix[i][k]):
                    return False
                k += 1
        return True