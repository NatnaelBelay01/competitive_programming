class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        

        def rec(i, j):

            if(i >= j):
                return ""
                #base-case

            check = set(s[i:j+1])

            for k in range(i, j+1):
                if( chr(ord(s[k]) + 32) not in check and chr(ord(s[k]) - 32) not in check):
                    val2 = rec(i, k-1)
                    val1 = rec(k+1 , j)
                    
                    return val2 if len(val2) >= len(val1) else val1
            return s[i:j+1]
        
        
        return rec(0, len(s) - 1)