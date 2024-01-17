class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        

        left = 0
        count = 0
        ans = float('inf')

        for right in range(len(blocks)):
            if(blocks[right] == 'W'):
                count += 1
            
            if(right - left + 1 > k):
                if(blocks[left] == 'W'):
                    count -= 1
                left += 1
            if(right - left + 1 == k):
                ans = min(ans , count)
        
        if(ans == float('inf')):
            return 0
        
        return ans