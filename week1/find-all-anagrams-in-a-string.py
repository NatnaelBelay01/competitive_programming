class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        check = {}

        for val in p:
            check[val] = 1 + check.get(val , 0)
        
        window = {}
        result = []

        leng = len(p)
        left = 0

        for right in range(len(s)):

            window[s[right]] = 1 + window.get(s[right] , 0)

            if( right - left + 1 > leng ):
                window[s[left]] -= 1
                if (window[s[left]] == 0):
                    window.pop(s[left])
                left += 1
            

            if (window == check):
                result.append(right - leng + 1 )

        return result
                
        