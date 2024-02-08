class Solution:
    def numberOfWays(self, s: str) -> int:

        zero_a = [0] * (len(s))
        ones_a = [0] * (len(s))

        idx = len(s) - 2

        while(idx >= 0):
            if(s[idx+1] == '1'):
                ones_a[idx] += ones_a[idx + 1] + 1
                zero_a[idx] += zero_a[idx + 1]
            else:
                ones_a[idx] += ones_a[idx+1]
                zero_a[idx] += zero_a[idx + 1] + 1
            idx -= 1
        
        count_one = 0
        count_zero = 0
        ans = 0


        for idx in range(len(s)):
            if(s[idx] == '0'):
                ans += count_one * ones_a[idx]
                count_zero += 1
            else:
                ans += count_zero * zero_a[idx]
                count_one += 1

        return ans


        