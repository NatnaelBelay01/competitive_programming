class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        

        val = 0

        for i in range(n-1):

            if k > (2 ** ( (n-i) - 1)) // 2:
                if val == 0:
                    val = 1
                else:
                    val = 0
            
                k -= (2 ** ((n-i) - 1) ) // 2

        
        return val
