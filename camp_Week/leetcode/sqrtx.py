class Solution:
    def mySqrt(self, x: int) -> int:
        
        l = -1
        r = x+1

        while (r > l + 1):

            m = (r + l) // 2

            if m * m > x:
                r = m
            else:
                l = m
        return l