class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:


        points.sort(key=lambda x:x[0])

        res = []
        res.append(points[0])

        for idx in range(1 , len(points)):
            if(points[idx][0] > res[-1][1]):
                res.append(points[idx])
            else:
                res[-1][1] = min(res[-1][1], points[idx][1])
                res[-1][0] = max(res[-1][1], points[idx][0])
        
        return len(res)

        
        