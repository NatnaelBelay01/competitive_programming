class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        

        tot = sum(nums)
        if(tot < p):
            return -1
        k = tot %  p

        if (k == 0):
            return 0

        store = {}
        store[0] = -1
        presum = 0

        ans = float('inf')


        for idx in range(len(nums)):
            presum = (nums[idx] + presum) % p 
            if((presum - k) % p in store):
                ans = min(ans, idx - store[(presum - k) % p] )
            store[presum ] = idx 
        
        if ans == float('inf'):
            return -1
        return ans if ans < len(nums) else -1