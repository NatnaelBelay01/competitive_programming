class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s) // 4

        count = collections.Counter(s)

        extra = {}

        for val in count:
            if count[val] > n:
                extra[val] = count[val] - n
        

        if extra == {}:
            return 0
        left = 0
        ans = float('inf')

        for right in range(len(s)):
            if (s[right] in extra):
                extra[s[right]] -= 1
            
            while(max(extra.values()) <= 0):
                ans = min(ans, right - left + 1)
                if(s[left] in extra):
                    extra[s[left]] += 1
                left += 1
        
        if ans == float("inf"):
            return 0
        return ans