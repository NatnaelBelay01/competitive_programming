class RandomizedSet:

    def __init__(self):
        self.randlist = []
        self.randdict = {}

    def insert(self, val: int) -> bool:
        if (val not in self.randdict):
            self.randdict[val] = len(self.randlist)
            self.randlist.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if (val in self.randdict):
            idx = self.randdict[val]
            self.randlist[-1] , self.randlist[idx] = self.randlist[idx] , self.randlist[-1]
            self.randdict[self.randlist[idx]] = idx
            self.randlist.pop()
            self.randdict.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        idx = random.randint(0 , len(self.randlist)-1)
        return self.randlist[idx]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()