class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        runSum = [0] * (len(s))

        for val in shifts:
            if(val[2] == 1):
                runSum[val[0]] += 1
                if val[1] + 1 < len(s):
                    runSum[val[1] + 1] -= 1
            else:
                runSum[val[0]] -= 1
                if val[1] + 1 < len(s):
                    runSum[val[1] + 1] += 1
        
        for i in range(1, len(s)):
            runSum[i] += runSum[i-1]

        for idx in range(len(s)):
            runSum[idx]= chr( ((ord(s[idx]) - 97) + runSum[idx]) % 26  + ord('a'))
        
        return "".join(runSum)
        



        return ""