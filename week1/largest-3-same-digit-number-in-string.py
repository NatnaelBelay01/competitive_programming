class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = 0
        l = len(num)
        res = float('-inf')
        check = []
        for i in range(l):
            check.append(int(num[i]))
            if i > 1:
                if min(check) == max(check):
                    res = max(res , max(check))
                check.pop(0)
        if res == float('-inf'):
            return ""
        return str(res) * 3