class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        presum  = 0
        ans = float('-inf')

        for idx in range(len(nums)):
            presum += nums[idx]
            ans = max(ans , presum)
            if(presum < 0):
                presum = 0
        return ans