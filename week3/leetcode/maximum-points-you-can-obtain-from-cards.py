class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        front = 0
        back = sum(cardPoints[ len(cardPoints) - k:])

        ans = front + back
        print(ans)
        leng = len(cardPoints) - k

        for idx in range(k):
            front += cardPoints[idx]
            back -= cardPoints[idx + leng]
            ans = max(front + back, ans)
        
        return ans

