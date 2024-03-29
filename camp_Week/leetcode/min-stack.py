class MinStack:

    def __init__(self):
        self.stack =[]
        self.mstack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if(not self.mstack or val <= self.mstack[-1]):
            self.mstack.append(val)
        

    def pop(self) -> None:
        val = self.stack.pop()

        if self.mstack[-1] == val:
            self.mstack.pop()
        
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()