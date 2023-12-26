class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        
        count = 0
        big = 0

        for idx in range(len(flips)):
            big = max(big , flips[idx])

            if(big == idx + 1):
                count += 1
        return count