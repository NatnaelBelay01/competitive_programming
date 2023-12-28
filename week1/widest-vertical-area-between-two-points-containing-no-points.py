class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:

        points.sort(key=lambda x:x[0])

        result = 0

        for idx in range(1, len(points)):
            width = points[idx][0] - points[idx-1][0]
            result = max(result , width)
        return result
