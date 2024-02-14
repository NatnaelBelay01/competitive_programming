class Node:
    def __init__(self, val = "", next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev


class BrowserHistory:

    def __init__(self, homepage: str):

        self.homepage = Node(homepage)
        self.curr = self.homepage

    def visit(self, url: str) -> None:
        node = Node(url, None, self.curr)
        self.curr.next = node
        self.curr = self.curr.next


    def back(self, steps: int) -> str:

        while(steps and self.curr.prev):
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val
        

    def forward(self, steps: int) -> str:
        
        while(self.curr.next and steps):
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)