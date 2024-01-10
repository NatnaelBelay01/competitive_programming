class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0

        tot = 0
        res = float('inf')


        for right in range(len(nums)):
            tot += nums[right]

            while(tot >= target):
                res = min(res , right - left + 1)
                tot -= nums[left]
                left += 1

        
        if(res == float('inf')):
            return 0
        
        return res