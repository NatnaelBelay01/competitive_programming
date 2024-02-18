class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:

        arr = []

        for idx in range(1 , len(weights)):
            arr.append(weights[idx] + weights[idx-1])
        
        arr.sort()

        maxscore = 0
        
        minscore = sum(arr[:k - 1])

        j = len(arr) - 1
        c = k - 1

        while(c > 0):
            maxscore += arr[j]
            j -= 1
            c -= 1
        return maxscore - minscore
        
        