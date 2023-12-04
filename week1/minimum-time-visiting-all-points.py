class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        l = len(points)
        for i in range(1, l):
            a = abs(points[i][0] - points[i-1][0])
            b = abs(points[i][1] - points[i-1][1])
            ans += max(a, b)
        return ans