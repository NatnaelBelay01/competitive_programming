class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check = {'{':'}', '(':')', '[':']'}
        for i in s:
            if (i in check):
                stack.append(i)
            else:
                if stack and i == check[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0