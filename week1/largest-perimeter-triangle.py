class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        idx = len(nums) - 1

        while (idx > 1):
            if (nums[idx] - (nums[idx - 1] + nums[idx - 2]) >= 0):
                idx -= 1
            else:
                return nums[idx] + nums[idx-1] + nums[idx-2]
        return 0