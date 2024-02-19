class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        check = {'+' , '*' , '/',  '-'}

        for i in tokens:
            
            if i in check:
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append( str(int(eval(val2 + i + val1))) )
            else:
                stack.append(i)
        
        return int(stack[0])