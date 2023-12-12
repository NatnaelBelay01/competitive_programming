class Solution:
    def isHappy(self, n: int) -> bool:
        check = set()
        while (True):
            lst = []
            total = 0
            for i in str(n):
                lst.append(int(i))
            for num in lst:
                total += num**2
            n = total
            if (n == 1):
                return True
            if n in check:
                return False
            check.add(n)