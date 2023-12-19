class ATM:

    def __init__(self):
        self.notes = [20, 50, 100, 200, 500]
        self. balance = [0 , 0, 0, 0, 0]
    def deposit(self, banknotesCount: List[int]) -> None:
        for idx in range(len(banknotesCount)):
            self.balance[idx] += banknotesCount[idx]

    def withdraw(self, amount: int) -> List[int]:
        ops = [0] * 5
        for idx in range(len(self.balance)-1, -1, -1):
            check = amount // self.notes[idx]
            amount -= min(check , self.balance[idx]) * self.notes[idx]
            ops[idx] += min(check, self.balance[idx])
            if(amount <= 0):
                break
        if(amount != 0):
            return [-1]
        else:
            for idx in range(len(ops)):
                self.balance[idx] -= ops[idx]
            return ops

        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)