class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        presum = [0] * len(nums)

        for val in requests:
            presum[val[0]] += 1
            if(val[1] + 1 < len(nums)):
                presum[val[1] + 1] += -1
        
        
        for idx in range(1 ,len(nums)):
            presum[idx] += presum[idx - 1]
        
        presum.sort()
        nums.sort()

        idx = len(presum) - 1
        ans = 0

        while(idx >= 0):
            if(presum[idx] == 0):
                break
            ans += presum[idx] * nums[idx]
            idx -= 1
        
        return ans % (10**9 + 7)