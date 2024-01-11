class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        front = [0] * (len(cardPoints) + 1)
        back = [0] * (len(cardPoints) + 1)

        for idx in range(len(cardPoints)):
            front[idx + 1] = front[idx] + cardPoints[idx]
        
        for idx in range(len(cardPoints) - 1 , -1 , -1):
            back[idx] = back[ idx + 1 ] + cardPoints[idx]
        
        ans = 0


        tot = 0
        for idx in range(k+1):
           ans = front[idx] + back[len(back) - 1 - k + idx]
           tot = max(ans , tot)

        return tot
