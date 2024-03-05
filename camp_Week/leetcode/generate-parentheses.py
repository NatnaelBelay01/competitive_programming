class Solution:
    def generateParenthesis(self, n: int) -> List[str]:


        self.ans = []        
        
        
        def back(openp , closep , path):


            if len(path) == 2 * n:

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