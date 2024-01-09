class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        check = { 'a', 'e', 'i' , 'o', 'u' }

        left = 0
        res = 0
        window = {'c':0 , 'v':0}

        for right in range(len(s)):

            if(s[right] in check):
                window['v'] += 1
            else:
                window['c'] += 1

            if (right - left + 1 > k):
                if(s[left] in check):
                    window['v'] -= 1
                else:
                    window['c'] -= 1
                left += 1
            
            res = max(res , window['v'])
        
        return res
