class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        countZ = 0
        left = 0
        result = 0


        for right in range(len(nums)):
            if(nums[right] == 0):
                countZ += 1
            
            while(countZ > k):
                if(nums[left] == 0):
                    countZ -= 1
                left += 1
            
            result = max(result, right - left + 1)
        
        return result