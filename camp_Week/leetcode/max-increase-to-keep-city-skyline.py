class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        top = [0] * n
        side = [0] * n

        for r in range(n):
            temp = 0
            for c in range(n):
                temp = max(temp, grid[r][c])
            side[r] = temp

        for c in range(n):
            temp = 0
            for r in range(n):
                temp = max(temp, grid[r][c])
            top[c] = temp

        ans = 0

        for r in range(n):
            for c in range(n):
                ans += min(top[c] , side[r]) - grid[r][c]
        return ans