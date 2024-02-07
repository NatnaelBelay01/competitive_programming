class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        before = [1]*len(nums)
        after = [1]*len(nums)

        idx = len(nums) - 2
        while (idx >= 0):
            after[idx] = nums[idx + 1] * after[idx + 1]
            idx -= 1
        
        idx = 1

        while (idx < len(nums)):
            before[idx] = before[idx - 1] * nums[idx - 1]
            idx += 1
        
        for idx in range(len(nums)):
            after[idx] *= before[idx]
        
        return after
        