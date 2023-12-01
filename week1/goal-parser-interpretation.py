class Solution:
    def interpret(self, command: str) -> str:
        i = 0
        lst = list(command)
        out = []
        stack = []
        for i in lst:
            stack.append(i)
            if (stack[-1] == ')'):
                while (stack[-1] != '('):
                    out.append(stack.pop())
                out.append(stack.pop())
                if (out == [')', '(']):
                    stack.append('o')
                    out = []
                else:
                    stack.append('a')
                    stack.append('l')
                    out = []
        return "".join(stack)