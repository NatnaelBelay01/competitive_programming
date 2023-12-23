class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def helper(board, row, col):
            check = set()
            for roww in range(row ,row+3):
                for coll in range(col, col+3):
                    if (board[roww][coll] != "." and board[roww][coll] in check):
                        return False
                    if (board[roww][coll] != "."):
                        check.add(board[roww][coll])
            return True
        for col in range(9):
            cols_check = set()
            for row in range(9):
                if (board[row][col] != "." and board[row][col] in cols_check):
                    return False
                if(board[row][col] != "."):
                    cols_check.add(board[row][col])

        for row in range(9):
            rows_check = set()
            for col in range(9):
                if (board[row][col] != "." and board[row][col] in rows_check):
                    return False
                if(board[row][col] != "."):
                    rows_check.add(board[row][col])
        for row in range(0,9,3):
            for col in range(0,9,3):

                if (not helper(board, row, col)):
                    return False
        return True
        