class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        
        r = len(nums)
        l = -1

        while(r > l + 1):

            mid = (r + l) // 2

            if nums[mid] >= target:
                r = mid
            else:
                l = mid
        
        return r