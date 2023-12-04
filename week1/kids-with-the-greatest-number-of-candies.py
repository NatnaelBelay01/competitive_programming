class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        res = [0] * n
        max_can = max(candies)
        for i in range(n):
            res[i] = candies[i] + extraCandies >= max_can
        return res