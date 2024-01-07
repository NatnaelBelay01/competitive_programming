class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        check = {}
        first = 0
        result = 0

        
        for idx in range(len(s)):
            check[s[idx]] = 1 + check.get(s[idx] , 0)

            while(len(check) < idx - first + 1):
                check[s[first]] -= 1

                if (check[s[first]] == 0):
                    check.pop(s[first])
                first += 1
            
            result = max(result , idx - first + 1)
        
        return result