class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        first , last , idx = 0 , len(nums) - 1 , 0

        while (idx <= last):

            if (nums[idx] == 0):
                nums[idx] , nums[first] = nums[first] , nums[idx]
                idx += 1
                first += 1
            elif (nums[idx] == 2):
                nums[idx] , nums[last] = nums[last] , nums[idx]
                last -= 1
            else:
                idx += 1
        return nums




        