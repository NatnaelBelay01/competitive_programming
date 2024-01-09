class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        counT = 0
        counF = 0
        left = 0
        res = 0

        for right in range(len(answerKey)):

            if(answerKey[right] == 'T'):
                counT += 1
            else:
                counF += 1
            
            check = min(counT, counF)

            while(check > k):
                if(answerKey[left] == 'T'):
                    counT -= 1
                else:
                    counF -= 1
                left += 1

                check = min(counT, counF)

            res = max(res , right - left + 1)
        
        return res
            
