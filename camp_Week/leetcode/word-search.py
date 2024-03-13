class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        self.res = False

        
        def rec (path, row , col):

            if row >= len(board) or col >= len(board[0]):
                return
            if row < 0 or col < 0:
                return
            if len(path) > len(word):
                return

            
            if "".join(path) == word:
                self.res = True
                return

            if len(path) < len(word) and row < len(board) and col < len(board[0]) and word[len(path)] != board[row][col]:
                return
            
            if(0 <= row < len(board) and 0 <= col < len(board[0])):
                path.append(board[row][col])
                board[row][col] = '#'
                rec(path, row+1, col)
                rec(path, row, col+1)
                rec(path, row-1, col)
                rec(path, row, col-1)
                board[row][col] = path.pop()
        

        for row in range(len(board)):
            for col in range(len(board[0])):
                if "".join(board[row][col]) == word:
                    return True
                elif board[row][col] == word[0]:
                    rec([], row, col)
        

        return self.res