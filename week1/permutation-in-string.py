class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        check = {}
        check2 = {}

        for val in s1:
            check[val] = 1 + check.get(val, 0)
        
        leng = len(s1)
        left = 0

        for right in range(len(s2)):
            check2[s2[right]] = 1 + check2.get(s2[right], 0)

            if (right - left + 1 > leng):
                check2[s2[left]] -= 1
                if(check2[s2[left]] == 0):
                    check2.pop(s2[left])
                left += 1
            
            
            if(check2 == check):
                return True
        
        return False