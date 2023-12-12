class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        twice = set()
        for idx in range(len(fronts)):
            if fronts[idx] == backs[idx]:
                twice.add(fronts[idx])
        result = float('inf')

        for val in fronts+backs:
            if val not in twice:
                result = min(result, val)
        if (result == float('inf')):
            return 0
        return result