class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        good = len(nums) - 1

        i = len(nums) - 2

        while(i >= 0):
            if(i + nums[i] >= good):
                good = i
            i -= 1
        if(good == 0):
            return True
        else:
            return False