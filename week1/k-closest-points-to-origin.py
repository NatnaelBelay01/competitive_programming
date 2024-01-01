class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dist = [0] * len(points)
        points.sort(key=lambda points: (points[0]**2 + points[1]**2)**0.5)
        ans = []
        for idx in range(k):
            ans.append(points[idx])
        
        return ans