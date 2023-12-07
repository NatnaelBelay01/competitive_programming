class Solution:
    def largestOddNumber(self, num: str) -> str:
        idx = len(num) - 1

        while (idx >= 0):
            if (int(num[idx]) % 2 == 1):
                break
            idx -= 1
        if(idx == -1):
            return ""
        return num[:idx+1]