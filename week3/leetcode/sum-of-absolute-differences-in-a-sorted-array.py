class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        

        before = [0]*len(nums)
        after = [0]*len(nums)

        for idx in range(1, len(nums)):
            before[idx] = before[idx-1] + nums[idx-1]
        
        idx = len(nums) - 2

        while(idx >= 0):
            after[idx] = nums[idx + 1] + after[idx + 1]
            idx -= 1
        
        ans = 0

        for idx in range(len(nums)):
            last = len(nums) - (idx + 1)
            after[idx] = ( (idx * nums[idx]) - before[idx] ) + (after[idx] - (nums[idx] * last))
        
        return (after)

