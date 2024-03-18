class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def is_valid(n):
            check = 0
            for val in nums:
                check += math.ceil(val / n)
            return check <= threshold
        

        r = 1000000
        l = 0

        while(r > l + 1):
            mid = (r + l) // 2

            if is_valid(mid):
                r = mid
            else:
                l = mid
        
        return r
