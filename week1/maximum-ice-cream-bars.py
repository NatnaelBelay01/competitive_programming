class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = 0
        costs.sort()

        for val in costs:
            if(val <= coins):
                coins -= val
                count += 1
            else:
                break
        return count