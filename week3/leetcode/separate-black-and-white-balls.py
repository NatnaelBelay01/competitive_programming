class Solution:
    def minimumSteps(self, s: str) -> int:

        left = len(s) - 1
        right = len(s) - 1
        count = 0

        while (left >= 0):
            if(right == '1'):
                right -= 1
                if(right < left):
                    left = right - 1
                continue
            else:
                while(left >= 0 and s[left] == '0'):
                    left -= 1
                if(left >= 0):
                    count += right - left
                    right -= 1
                    left -= 1
        
        return count
        