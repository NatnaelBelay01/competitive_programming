class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        allSum = {}
        allSum[0] = 1
        presum = 0
        ans = 0

        for idx in range(len(nums)):

            presum += nums[idx]

            if(presum - k in allSum):
                ans += allSum[presum-k]
            allSum[presum] = 1 + allSum.get(presum, 0)
        
        return ans
        