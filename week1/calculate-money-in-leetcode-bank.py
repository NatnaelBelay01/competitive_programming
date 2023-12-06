class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        money = 0
        idx = 0
        count = 1
        days = [i for i in range(1,8)]

        while (count <= n):
            total += days[idx] + money
            if (count % 7 == 0):
                money += 1
            count += 1
            idx = (idx+1) % 7
        return total