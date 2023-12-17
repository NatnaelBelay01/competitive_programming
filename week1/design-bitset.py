class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.ones = set()
        self.zeros = {i for i in range(size)}
        
    def fix(self, idx: int) -> None:
        if (idx not in self.ones):
            self.ones.add(idx)
            self.zeros.discard(idx)

    def unfix(self, idx: int) -> None:
        if (idx not in self.zeros):
            self.zeros.add(idx)
            self.ones.discard(idx)

    def flip(self) -> None:
        self.zeros , self.ones = self.ones , self.zeros 
        
    def all(self) -> bool:
        return len(self.ones) == self.size
    def one(self) -> bool:
        return len(self.ones) > 0
        

    def count(self) -> int:
        return len(self.ones)

    def toString(self) -> str:
        result = ['0'] * self.size
        for idx in self.ones:
            result[idx] = '1'
        return "".join(result)
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()