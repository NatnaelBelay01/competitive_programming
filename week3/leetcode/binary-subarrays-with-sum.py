class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        ans = 0

        store = {}
        store[0] = 1

        presum = 0

        for right in range(len(nums)):
            presum += nums[right]

            if(presum - goal in store):
                ans += store[presum - goal]
            store[presum] = 1 + store.get(presum , 0)
        
        return ans
