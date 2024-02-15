class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        answers.sort()
        
        res = answers[0]+1
        bud = answers[0]
        idx = 1

        while(idx < len(answers)):
            if(answers[idx] != answers[idx-1] or bud <= 0):
                res += answers[idx] + 1
                bud = answers[idx]
            else:
                bud -= 1
            idx += 1
        return res
