class Solution:
    def minWindow(self, s: str, t: str) -> str:

        ans = float('inf')
        left = 0
        check = {}
        formed = 0
        
        ret = [float('inf') , 0]

        for val in range(len(t)):
            check[t[val]] = 1 + check.get(t[val] , 0)

        req = len(check)
        window = {}


        for right in range(len(s)):

            window[s[right]] = 1 + window.get(s[right], 0)
            
            if s[right] in check and check[s[right]] == window[s[right]]:
                formed += 1
            
            while(formed == req):
                if(ret[0] - ret[1] + 1 > right - left + 1):
                    ret[0] = right
                    ret[1] = left
                window[s[left]] -= 1
                if(s[left] in check and window[s[left]] < check[s[left]]):
                    formed -= 1
                left += 1
        if(ret[0] == float('inf')):
            return ""
        return s[ret[1] : ret[0] + 1]
        