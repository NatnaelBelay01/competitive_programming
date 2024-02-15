class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        
        if maxDoubles == 0:
            return target - 1

        res = 0
        while(maxDoubles > 0 and target > 1):
            
            if target % 2 != 0:
                res += 1
            target //= 2
            res += 1
            maxDoubles -= 1
        if target > 1:
            res += target - 1
        
        return res

