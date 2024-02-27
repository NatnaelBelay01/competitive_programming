class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        if n == 1:
            return ['()']

        self.ans = []        
        
        
        def back(openp , closep , path):


            if len(path) == 2 * n:
                #the base case
                #check validity
                #if valid append else quit
                if 1:
                   self.ans.append("".join(path[:])) 
                return
            if closep < openp:
                return
            check = []
            if openp > 0:
                check.append('(')
            if closep > 0:
                check.append(')')

            for choice in check:
                path.append(choice)
                if choice == '(':
                    back(openp - 1 , closep, path)
                else:
                    back(openp, closep - 1, path)
                path.pop()
        

        back(n , n, [])

        return self.ans