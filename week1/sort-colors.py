class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        first, mid ,last = 0, 0, len(nums) - 1


        while(mid <= last):
            if(nums[mid] == 2):
                nums[last] , nums[mid] = nums[mid] , nums[last]
                last -= 1
            elif(nums[mid] == 0):
                nums[first] , nums[mid] = nums[mid] , nums[first]
                mid += 1
                first += 1
            else:
                mid += 1

        return nums



        