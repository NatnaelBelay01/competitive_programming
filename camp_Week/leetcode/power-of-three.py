class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        def rec(n):

            if n == 1:
                return True
            if n == 0:
                return False
            if n % 3 != 0:
                return False
            return rec(n // 3)
        
        return rec(n)