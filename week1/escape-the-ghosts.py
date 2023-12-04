class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        dist = float('inf')
        for i in ghosts:
            x = target[0] - i[0]
            y = target[1] - i[1]
            dist = min(abs(x) + abs(y), dist)
        return abs(target[0]) + abs(target[1]) < dist