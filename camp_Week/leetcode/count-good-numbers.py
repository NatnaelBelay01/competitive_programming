class Solution:
    def countGoodNumbers(self, n: int) -> int:

        MOD = (10**9) + 7
        def poww(b , e ):
            mod = 1000000007
            if e == 1:
                return b
            if e == 0:
                return 1

            if(e % 2 == 0):
                return poww( (b * b) % mod , e // 2)
            else:
                return b * poww( (b * b) % mod , (e - 1) // 2)


        
        if n == 1:
            return 5
        ev = n // 2

        res = poww(20 , ev)
        if n % 2 == 0:
            return res % MOD
        else:
            return (res * 5) % MOD
            
        