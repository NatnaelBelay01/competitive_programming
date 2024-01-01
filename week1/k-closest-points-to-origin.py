class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dist = []
        ans = []
        
        for idx , val in enumerate(points):
            dist.append([idx, (points[idx][0]**2 + points[idx][1]**2)**0.5])
 

        dist.sort(key=lambda x: x[1])
        
        
        for idx in range(k):
            ans.append(points[dist[idx][0]])
        
        return ans