class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left = 0

        while (left < len(nums) - 1):
            if (nums[left] == 0):
                right = left

                while (right < len(nums) and nums[right]  == 0):
                    right += 1
                if(right < len(nums)):
                    nums[right] , nums[left] = nums[left] , nums[right]
            left += 1
        return nums

                
        