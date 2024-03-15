class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def is_valid(n):
            
            check = 0
            res = 1
            for idx in range(len(weights)):
                if weights[idx] > n:
                    return False
                check += weights[idx]
                if check > n and res < days:
                    res += 1
                    check = weights[idx]
                elif check > n and res >= days:
                    return False
            return True
        

        d = (len(weights) - 1) // days + 1
        r = max(weights) * d
        l = min(weights)
        while(l < r):
            mid = (l + r) // 2
            if is_valid(mid):
                r = mid
            else:
                l = mid + 1
        
        print(is_valid(l))
        return l

