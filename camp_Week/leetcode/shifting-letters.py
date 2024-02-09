class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        presum = [0] * len(s)

        for idx in range(len(shifts)):
            presum[0] += shifts[idx]
            if(idx + 1 < len(shifts)):
                presum[idx + 1] -= shifts[idx]
        
        for idx in range(1 , len(presum)):
            presum[idx] += presum[idx - 1]

        for idx in range(len(s)):
            temp = ( (ord(s[idx]) - ord('a')) + presum[idx] ) % 26
            presum[idx] = chr(temp + ord('a'))


        return "".join(presum)