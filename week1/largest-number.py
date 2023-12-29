class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        for idx in range(len(nums)):
            nums[idx] = str(nums[idx])

        for idx in range(1 , len(nums)):
            new = idx
            while (new > 0 and nums[new - 1] + nums[new] <= nums[new] + nums[new-1]):
                nums[new] , nums[new - 1] = nums[new - 1], nums[new]
                new -= 1
        
        result = "".join(nums)
        if (result in "0"*100):
            return "0"
        return result
        