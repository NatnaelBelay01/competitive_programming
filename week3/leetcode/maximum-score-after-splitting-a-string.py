class Solution:
    def maxScore(self, s: str) -> int:

        ans = 0

        for idx in range(1, len(s)):
            left = s[:idx].count('0')
            right = s[idx:].count('1')
            ans = max(ans , right + left)
        return ans
        