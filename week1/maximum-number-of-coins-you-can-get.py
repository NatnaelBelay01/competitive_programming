class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        left = 0
        mid = n - 2
        res = 0
        while (mid > left):
            res += piles[mid]
            mid -= 2
            left += 1
        return res