class OrderedStream:

    def __init__(self, n: int):
        self.length = n
        self.lst = [' '] * n
        self.ptr = 0
    def insert(self, idKey: int, value: str) -> List[str]:
        self.lst[idKey - 1] = value
        result = []
        while ( self.ptr < self.length and self.lst[self.ptr] != ' '):
            result.append(self.lst[self.ptr])
            self.ptr += 1
        return result
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)