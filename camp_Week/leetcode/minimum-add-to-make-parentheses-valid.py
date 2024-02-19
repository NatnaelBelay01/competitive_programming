class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        ops = 0
        clos = 0


        for val in s:
            
            if( val == '('):
                clos += 1
            elif ( val == ')'):
                if clos == 0:
                    ops += 1
                else:
                    clos -= 1
            
        
        return ops + clos

