class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:

        tot = sum(nums)
        presum = 0

        for idx in range(len(nums)):

            if(presum == tot - (presum + nums[idx])):
                return idx
            presum += nums[idx]
        return -1
        