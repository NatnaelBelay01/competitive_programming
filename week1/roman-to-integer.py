class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        check = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        total = 0
        for i in range(len(s)):
            if i + 1 == len(s) or check[s[i+1]] <= check[s[i]]:
                total += check[s[i]]
            else:
                total += -1 * check[s[i]]
        return total