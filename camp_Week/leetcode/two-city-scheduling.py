class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs.sort(key=lambda x:x[0]- x[1])
        n = len(costs)
        res = 0
        count = 0

        for val in costs:
            count += 1
            if count <= n//2:
                res += val[0]

            else:
                res += val[1]
        
        return res