class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for row in range(len(matrix)):
            for col in range(row,len(matrix)):
                matrix[col][row],matrix[row][col] = matrix[row][col] , matrix[col][row]
        for i in range(len(matrix)):
            matrix[i]=matrix[i][::-1]
        
        